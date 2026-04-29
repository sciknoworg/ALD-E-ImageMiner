"""
Sci-ImageMiner Evaluation Script

Licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).
You may obtain a copy of the License at:

    https://creativecommons.org/licenses/by/4.0/

Unless required by applicable law or agreed to in writing, this software is
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied.
"""


"""Metrics functions for Sci-ImageMiner task evaluations."""

import re
import string
import numpy as np
import evaluate
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from teds_pubtables import teds_pubtables_official
from deplot_metric import metrics as deplot_metrics


def score_factoid(metrics):
    rouge_scores = np.array([
        metrics["rouge1"],
        metrics["rouge2"],
        metrics["rougeL"]
    ], dtype=np.float32)

    rouge_mean = rouge_scores.mean()
    exact_match = metrics["exact_match"]

    return 0.5 * rouge_mean + 0.5 * exact_match

def score_paragraph(metrics):
    rouge_scores = np.array([
        metrics["rouge1"],
        metrics["rouge2"],
        metrics["rougeL"]
    ], dtype=np.float32)

    rouge_mean = rouge_scores.mean()
    bert_f1 = metrics["bertscore_f1"]

    return 0.5 * rouge_mean + 0.5 * bert_f1

def score_list(metrics):
    return float(metrics["set-based-f1"])

def score_yes_no(metrics):
    vals = np.array(
        [metrics["accuracy"], metrics["f1_score"]],
        dtype=np.float32
    )
    return vals.mean()

def weighted_mean(values, weights):
    keys = [k for k in values if k in weights]
    if not keys:
        return 0.0

    v = np.array([values[k] for k in keys], dtype=np.float32)
    w = np.array([weights[k] for k in keys], dtype=np.float32)

    return float(np.dot(v, w) / w.sum())

def compute_weighted_score(metric_scores, answer_type_weights):
    scores = {}

    if "factoid" in metric_scores:
        scores["factoid"] = score_factoid(
            metric_scores["factoid"]
        )

    if "list" in metric_scores:
        scores["list"] = score_list(
            metric_scores["list"]
        )

    if "paragraph" in metric_scores:
        scores["paragraph"] = score_paragraph(
            metric_scores["paragraph"]
        )

    if "yesno" in metric_scores:
        scores["yesno"] = score_yes_no(
            metric_scores["yesno"]
        )

    return weighted_mean(scores, answer_type_weights)


def normalize_text(s):
    s = s.lower().strip()
    s = ''.join(ch for ch in s if ch not in string.punctuation)
    s = re.sub(r'\b(a|an|the)\b', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def extract_number(s):
    match = re.search(r'-?\d+(?:\.\d+)?', s)
    return float(match.group()) if match else None

def flatten_markdown_table(markdown_table):
    """Flatten a markdown table to a linearized string format compatible with DePlot RMS."""
    if not markdown_table:
        return ""

    lines = markdown_table.split('\n')
    separator_pattern = re.compile(r'^\|[-:\s]+\|[-:\s|]*\|$')
    
    cleaned_lines = []
    for line in lines:
        if separator_pattern.match(line):
            continue
        
        cleaned_line = line.strip().strip('|').strip()
        cleaned_lines.append(cleaned_line)
    
    return '\n'.join(cleaned_lines)


def compute_datatable_metrics(groundtruths, predictions, rounding=False, round_digits=2):
    if (len(predictions) == 0) or (len(groundtruths) == 0):
        return {
                "rms": 0.0,
                "teds": 0.0
            }
    else:
        rms_scores = []
        teds_pubtables_scores = []

        for truth, pred in zip(groundtruths, predictions):
            if truth.strip() == "":
                continue

            if not pred:
                rms_scores.append(0.0)
                teds_pubtables_scores.append(0.0)
            else:
                # RMS metric
                _target = flatten_markdown_table(truth)
                _prediction = flatten_markdown_table(pred)
                rms = deplot_metrics.table_datapoints_precision_recall([[_target]], [_prediction]) # RMS

                rms_scores.append(float(rms["table_datapoints_f1"]))

                # TEDS metrics
                teds_pubtables_scores.append(teds_pubtables_official(truth, pred) * 100) # since teds is usually normalized
            
        # Mean metrics
        if rounding:
            mean_rms = round(float(np.mean(np.array(rms_scores))), round_digits)
            mean_teds_pubtables = round(float(np.mean(np.array(teds_pubtables_scores))), round_digits)
        else:
            mean_rms = float(np.mean(np.array(rms_scores)))
            mean_teds_pubtables = float(np.mean(np.array(teds_pubtables_scores)))

        return {
            "rms": mean_rms,
            "teds": mean_teds_pubtables
        }


def metric_accuracy_precision_recall_f1(predictions, groundtruths, labels, average="micro", rounding=False, round_digits=2):
    if (len(predictions) == 0) or (len(groundtruths) == 0):
        return {
                "accuracy": 0.0,
                "precision": 0.0,
                "recall": 0.0,
                "f1_score": 0.0,
            }
    else:
        if rounding:
            return {
                "accuracy": round(accuracy_score(groundtruths, predictions), round_digits),
                "precision": round(precision_score(groundtruths, predictions, labels=labels, average=average, zero_division=0), round_digits),
                "recall": round(recall_score(groundtruths, predictions, labels=labels, average=average, zero_division=0), round_digits),
                "f1_score": round(f1_score(groundtruths, predictions, labels=labels, average=average, zero_division=0), round_digits),
            }
        else:
            return {
                "accuracy": accuracy_score(groundtruths, predictions),
                "precision": precision_score(groundtruths, predictions, labels=labels, average=average, zero_division=0),
                "recall": recall_score(groundtruths, predictions, labels=labels, average=average, zero_division=0),
                "f1_score": f1_score(groundtruths, predictions, labels=labels, average=average, zero_division=0),
            }

def metric_rouge(predictions, groundtruths, rouge_types=['rouge1', 'rouge2', 'rougeL'], rounding=False, round_digits=2):
    if (len(predictions) == 0) or (len(groundtruths) == 0):
        return {
                "rouge1": 0.0,
                "rouge2": 0.0,
                "rougeL": 0.0,
              }
    else:

        rouge = evaluate.load('rouge')
        scores = rouge.compute(predictions=predictions, references=groundtruths, rouge_types=rouge_types)

        result = {}

        if rounding:
            for k,v in scores.items():
                result[k] = round(float(v), round_digits)
        else:
            for k,v in scores.items():
                result[k] = float(v)

        return result

def metric_bertscore(predictions, groundtruths, model_type="distilbert-base-uncased", rounding=False, round_digits=2):
    if (len(predictions) == 0) or (len(groundtruths) == 0):
        return {
                "precision": 0.0,
                "recall": 0.0,
                "f1": 0.0
            }
    else:
        bertscore = evaluate.load("bertscore")
        scores = bertscore.compute(predictions=predictions, references=groundtruths,
                                model_type=model_type, use_fast_tokenizer=True, lang="en")
        
        if rounding:
            result = {
                "precision": round(float(np.mean(np.array(scores["precision"]))), round_digits),
                "recall": round(float(np.mean(np.array(scores["recall"]))), round_digits),
                "f1": round(float(np.mean(np.array(scores["f1"]))), round_digits)
            }
        else:
            result = {
                "precision": float(np.mean(np.array(scores["precision"]))),
                "recall": float(np.mean(np.array(scores["recall"]))),
                "f1": float(np.mean(np.array(scores["f1"])))
            }

        return result

def prf_from_comma_lists(pred_str, groundtruths_str):
    """
    Computes set-based Precision, Recall, and F1 for unordered comma-separated lists.
    """

    pred_list = [item.strip() for item in pred_str.split(",") if item.strip()]
    groundtruths_list = [item.strip() for item in groundtruths_str.split(",") if item.strip()]

    pred_set = set(pred_list)
    groundtruths_set = set(groundtruths_list)

    correct = pred_set.intersection(groundtruths_set)

    precision = len(correct) / len(pred_set) if pred_set else 0.0
    recall = len(correct) / len(groundtruths_set) if groundtruths_set else 0.0

    if precision + recall == 0:
        f1 = 0.0
    else:
        f1 = 2 * precision * recall / (precision + recall)

    return precision, recall, f1

def compute_paragraph_score(predictions, groundtruths, rounding=False, round_digits=2):
    if (len(predictions) == 0) or (len(groundtruths) == 0):
        return {
                "rouge1": 0.0,
                "rouge2": 0.0,
                "rougeL": 0.0,
                "bertscore_precision": 0.0,
                "bertscore_recall": 0.0,
                "bertscore_f1": 0.0
            }
    else:
        rouge = metric_rouge(predictions, groundtruths)
        bert = metric_bertscore(predictions, groundtruths)
        
        if rounding:
            return {
                "rouge1": round(float(rouge["rouge1"]), round_digits),
                "rouge2": round(float(rouge["rouge2"]), round_digits),
                "rougeL": round(float(rouge["rougeL"]), round_digits),
                "bertscore_precision": round(float(np.mean(np.array(bert["precision"]))), round_digits),
                "bertscore_recall": round(float(np.mean(np.array(bert["recall"]))), round_digits),
                "bertscore_f1": round(float(np.mean(np.array(bert["f1"]))), round_digits),
            }
        else:
            return {
                "rouge1": float(rouge["rouge1"]),
                "rouge2": float(rouge["rouge2"]),
                "rougeL": float(rouge["rougeL"]),
                "bertscore_precision": float(np.mean(np.array(bert["precision"]))),
                "bertscore_recall": float(np.mean(np.array(bert["recall"]))),
                "bertscore_f1": float(np.mean(np.array(bert["f1"]))),
            }

def exact_match(predictions, groundtruths, ignore_case=True, ignore_punctuation=False, ignore_numbers=False, rounding=False, round_digits=2):
    exact_match_metric = evaluate.load("exact_match")
    return exact_match_metric.compute(references=groundtruths, predictions=predictions, ignore_case=ignore_case, ignore_punctuation=ignore_punctuation, ignore_numbers=ignore_numbers)
    

def compute_factoid_score(predictions, groundtruths, numeric_tolerance=None, rounding=False, round_digits=2):
    if (len(predictions) == 0) or (len(groundtruths) == 0):
        return {
                "exact_match": 0.0,
                "rouge1": 0.0,
                "rouge2": 0.0,
                "rougeL": 0.0
            }
    else:
        exact_match_score = exact_match(predictions, groundtruths, ignore_case=True, ignore_numbers=False, ignore_punctuation=True)       
        rouge = metric_rouge(predictions, groundtruths)

        if rounding:
            return {
                "exact_match": round(float(exact_match_score["exact_match"]), round_digits),
                "rouge1": round(float(rouge["rouge1"]), round_digits),
                "rouge2": round(float(rouge["rouge2"]), round_digits),
                "rougeL": round(float(rouge["rougeL"]), round_digits)
            }
        else:
            return {
                "exact_match": float(exact_match_score["exact_match"]),
                "rouge1": float(rouge["rouge1"]),
                "rouge2": float(rouge["rouge2"]),
                "rougeL": float(rouge["rougeL"])
            }

def compute_yesno_score(predictions, groundtruths, labels=["yes", "no"], rounding=False, round_digits=2):

    pred_norm = [normalize_text(item) for item in predictions]
    groundtruths_norm =  [normalize_text(item) for item in groundtruths]

    return metric_accuracy_precision_recall_f1(groundtruths=groundtruths_norm, predictions=pred_norm, labels=["yes", "no"], rounding=rounding, round_digits=round_digits)

def compute_list_score(predictions, groundtruths, rounding=False, round_digits=2):
    if (len(predictions) == 0) or (len(groundtruths) == 0):
        return {
                "set-based-precision": 0.0,
                "set-based-recall": 0.0,
                "set-based-f1": 0.0
            }
    else:
        set_based_precision_scores = []
        set_based_recall_scores = []
        set_based_f1_scores = []

        for p, g in zip(predictions, groundtruths):
            precision, recall, f1 = prf_from_comma_lists(p, g)
            
            set_based_precision_scores.append(precision)
            set_based_recall_scores.append(recall)
            set_based_f1_scores.append(f1)


        if rounding:
            return {
                "set-based-precision": round(float(np.mean(np.array(set_based_precision_scores))), round_digits),
                "set-based-recall": round(float(np.mean(np.array(set_based_recall_scores))), round_digits),
                "set-based-f1": round(float(np.mean(np.array(set_based_f1_scores))), round_digits),
            }
        else:
            return {
                "set-based-precision": float(np.mean(np.array(set_based_precision_scores))),
                "set-based-recall": float(np.mean(np.array(set_based_recall_scores))),
                "set-based-f1": float(np.mean(np.array(set_based_f1_scores))),
            }


