"""
Sci-ImageMiner Evaluation Script

Licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).
You may obtain a copy of the License at:

    https://creativecommons.org/licenses/by/4.0/

Unless required by applicable law or agreed to in writing, this software is
distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied.
"""

import os
import sys
import argparse

import json
import os
import os.path
import re


from metrics import (
    metric_accuracy_precision_recall_f1,
    compute_datatable_metrics,
    compute_factoid_score,
    compute_list_score,
    compute_paragraph_score,
    compute_yesno_score,
    compute_weighted_score
)


schema = {
    "sample_id": str
}

VQA_ANSWER_TYPE_FACTOID = "factoid"
VQA_ANSWER_TYPE_PARAGRAPH = "paragraph"
VQA_ANSWER_TYPE_LIST = "list"
VQA_ANSWER_TYPE_YESNO = "yes/no"

SUPERSCRIPTS = {
    "⁰": "0",
    "¹": "1",
    "²": "2",
    "³": "3",
    "⁴": "4",
    "⁵": "5",
    "⁶": "6",
    "⁷": "7",
    "⁸": "8",
    "⁹": "9",
}

UNIT_NORMALIZATION = {
    "percent": "%",
    "percentage": "%",
    "wt%": "%",
    "mol%": "%",
    "x10^": "e",
    "*10^": "e",
    "x10^": "e",
}

CLASSES = (
    "area chart",
    "bar chart",
    "3d bar chart", 
    "grouped bar chart",
    "stacked bar chart",
    "box plot",
    "bubble chart",
    "donut chart",
    "funnel chart", 
    "heatmap",
    "line chart",
    "multiple line chart", 
    "multi-axis chart",
    "pie chart",
    "polar chart (rose chart)", 
    "radar chart (spider chart)",
    "3d scatter plot",
    "scatter plot",
    "multiple scatter plot"
    "treemap",
    "spectra chart",
    "stacked spectra chart",
    "multi spectra chart",
    "phase diagram", 
    "band diagram",
    "adsorption isotherm",
    "process timing diagram",
    "contour heatmap",
    "image panel",
    "map/geo chart",
    "molecular structure diagram",
    "reaction scheme",
    "process flow diagram",
    "reaction energy profile diagram",
    "apparatus diagram",
    "conceptual diagram",
    "device structure",
    "chromaticity diagram"
    "periodic table map",
    "element-property matrix",
    "network diagram",
    "tree diagram",
    "workflow diagram",
    "timeline chart",
    "comparison table",
    "formula",
    "table",
    "unknown"
)


def normalize(text: str) -> str:
    """
    Normalize the input text with unit normaliztion, superscripts, etc.
    
    Args:
        text (str): The input text to be normalized

    Returns:
        str: The normalized text.
    """

    if not text:
        return ""

    text = text.lower()

    for k, v in SUPERSCRIPTS.items():
        text = text.replace(k, v)

    for k, v in UNIT_NORMALIZATION.items():
        text = text.replace(k, v)

    text = re.sub(r"\$([^$]+)\$", r"\1", text)

    text = re.sub(r"(\d+(?:\.\d+)?)\s*[xx\*]\s*10\^(\d+)", r"\1e\2", text)

    text = re.sub(r"\s+", " ", text)
    return text.strip()


def load_json(file_path: str, encoding: str = 'utf-8'):
    """
    Reads the JSON file and return it's content.

    Args:
        file_path (str): The path to the JSON file
        encoding (str): The encoder to use for reading the file

    Returns:
        dict: The JSON file content.
    """
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            return json.load(f)
    except json.JSONDecodeError:
        print('Cannot parse JSON file: {}'.format(file_path))
    except FileNotFoundError:
        print('File Not Found: {}'.format(file_path))
    except Exception as e:
        print('Exception Occured: {}'.format(e))


def write_file(file_path: str, text: str):
    """
    Writes to the JSON file.

    Args:
        file_path (str): The path to the JSON file
        encoding (str): The encoder to use for reading the file

    Returns:
        dict: The JSON file content.
    """
    with open(file_path, 'a', encoding="utf-8") as f:
        f.write(text)


def decode_unicode(text: str) -> str:
    """
    Decode \\uXXXX escape sequences back to Unicode characters.

    Args:
        text (str): The path to the JSON file

    Returns:
        str: The decoded Unicode string.
    """
    if text is None:
        return ""

    if not isinstance(text, str):
        text = str(text)

    try:
        return bytes(text, "utf-8").decode("unicode_escape")
    except UnicodeDecodeError:
        return text


def is_empty(value):
    """
    Checks whether the value is empty. 
    """
    return value is None or str(value).strip() == ""


def validate_submission_schema(data, required_sample_keys):
    """
    Validates the submission data against the required schema.

    Args:
        text (str): The path to the JSON file

    Returns:
        str: The decoded Unicode string.
    """
    
    if not isinstance(data, list):
        raise ValueError("Submission must be a list of samples")

    for i, sample in enumerate(data):
        for key, typ in required_sample_keys.items():
            if key not in sample:
                raise ValueError(f"Invalid Submission Schema: missing '{key}'.\nSample: {sample}")
            if not isinstance(sample[key], typ):
                raise ValueError(f"Invalid Submission Schema: '{key}' must be {typ.__name__}.\nSample: {sample}")

    return True


def is_valid_markdown_table_strict(text: str) -> bool:
    """
    Validates the markdown table format.

    Args:
        text (str): The text to validate

    Returns:
        bool: True if valid, False otherwise.
    """

    if not text or not text.strip():
        return False

    lines = [line.rstrip() for line in text.splitlines() if line.strip()]
    if len(lines) < 2:
        return False

    def split_row(row):
        if not row.startswith("|") or not row.endswith("|"):
            return None

        return [cell.strip() for cell in row[1:-1].split("|")]

    header_cells = split_row(lines[0])
    sep_cells = split_row(lines[1])

    if header_cells is None or sep_cells is None:
        return False

    if len(header_cells) != len(sep_cells):
        return False

    for cell in sep_cells:
        if not re.fullmatch(r":?-+:?", cell):
            return False

    for row in lines[2:]:
        cells = split_row(row)
        if cells is None:
            return False
        if len(cells) != len(header_cells):
            return False

    return True

def parse_args():
    """
    Parses command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Sci-ImageMiner evaluate predictions against a reference dataset."
    )

    parser.add_argument(
        "--task",
        type=str,
        required=True,
        help="Task to evaluate (e.g. classification, data extraction, summarization, vqa)"
    )

    parser.add_argument(
        "--reference-path",
        type=str,
        required=True,
        help="Path to reference JSON"
    )

    parser.add_argument(
        "--prediction-path",
        type=str,
        required=True,
        help="Path to prediction JSON"
    )

    parser.add_argument(
        "--output-scores-path",
        type=str,
        required=True,
        help="Path to output scores JSON"
    )

    return parser.parse_args()


def main():
    args = parse_args()

    task = args.task
    reference_path = args.reference_path
    prediction_path = args.prediction_path
    output_scores_path = args.output_scores_path

    # Validate task
    if task not in ["classification", "data_extraction", "summarization", "vqa"]:
        raise ValueError(f"Invalid task: {task}. Must be one of: classification, data_extraction, summarization, vqa")

    # Validate paths
    if not os.path.exists(reference_path):
        raise FileNotFoundError(f"File doesn't exist: {reference_path}")
    if not os.path.exists(prediction_path):
        raise FileNotFoundError(f"File doesn't exist: {prediction_path}")


    print(f"Task: {task}")
    print(f"Reference path: {reference_path}")
    print(f"Prediction path: {prediction_path}")
    print(f"Output path: {output_scores_path}")
    print()

    # Load reference and prediction data
    references_data = load_json(reference_path)
    predictions_data = load_json(prediction_path)

    # Validate JSON schema (predictions)
    validate_submission_schema(predictions_data, required_sample_keys=schema)

    # Process and store per task data
    data = {}
    if task in ["classification", "data_extraction", "summarization"]:
        data = {
            "references": [],
            "predictions": []
        }
    elif task == "vqa":
        data = {
            VQA_ANSWER_TYPE_FACTOID: {"references": [], "predictions": []},
            VQA_ANSWER_TYPE_PARAGRAPH: {"references": [], "predictions": []},
            VQA_ANSWER_TYPE_LIST: {"references": [], "predictions": []},
            VQA_ANSWER_TYPE_YESNO: {"references": [], "predictions": []}
        }

    ref_map = {s["sample_id"]: s for s in references_data}
    pred_map = {s["sample_id"]: s for s in predictions_data}

    for sid, ref in ref_map.items():
        pred = pred_map.get(sid, {})

        if task == "classification":
            for panel, ref_cls in ref.get("classification", {}).items():
                pred_cls = pred.get("classification", {}).get(panel, None)

                if is_empty(pred_cls):
                    pred_cls = ""

                data["references"].append(decode_unicode(ref_cls))
                data["predictions"].append(decode_unicode(pred_cls))


        elif task == "summarization":
            for panel, ref_sum in ref.get("summarization", {}).items():
                pred_sum = pred.get("summarization", {}).get(panel, None)

                if is_empty(pred_sum):
                    pred_sum = ""

                data["references"].append(decode_unicode(ref_sum))
                data["predictions"].append(decode_unicode(pred_sum))


        elif task == "data_extraction":
            for panel, ref_tbl in ref.get("data_extraction", {}).items():
                pred_tbl = pred.get("data_extraction", {}).get(panel, None)

                if is_empty(pred_tbl) or not is_valid_markdown_table_strict(pred_tbl):
                    pred_tbl = ""

                data["references"].append(decode_unicode(ref_tbl))
                data["predictions"].append(decode_unicode(pred_tbl))


        elif task == "vqa":
            ref_vqa = ref.get("vqa", {})
            pred_vqa = pred.get("vqa", {})

            for label, ref_questions in ref_vqa.items():
                pred_questions = pred_vqa.get(label, [])

                pred_index = {
                    decode_unicode(normalize(q["question"])): q for q in pred_questions
                }

                for ref_question in ref_questions:
                    ref_question_normalized = decode_unicode(normalize(ref_question["question"]))
                    ref_question["question"] = ref_question_normalized
                    pred_question = pred_index.get(ref_question_normalized)

                    if not pred_question:
                        pred_question = {
                            "question_type": ref_question["question_type"],
                            "question": ref_question["question"],                        
                            "answer_type": ref_question["answer_type"],
                            "answer": "",
                        }

                    ref_question_type = ref_question["question_type"].lower()
                    ref_answer_type = ref_question["answer_type"].lower()

                    pred_question_type = pred_question["question_type"].lower()
                    pred_answer_type = pred_question["answer_type"].lower()

                    # set empty pred answer if pred question/answer type mismatch 
                    if (ref_question_type != pred_question_type):
                        pred_question["answer"] = ""
                    elif (ref_answer_type != pred_answer_type):
                        pred_question["answer"] = ""

                    # process answers
                    if ref_answer_type == VQA_ANSWER_TYPE_FACTOID:
                        data[VQA_ANSWER_TYPE_FACTOID]["references"].append(decode_unicode(ref_question.get("answer", "")))
                        data[VQA_ANSWER_TYPE_FACTOID]["predictions"].append(decode_unicode(pred_question.get("answer", "")))
                    elif ref_answer_type == VQA_ANSWER_TYPE_PARAGRAPH:
                        data[VQA_ANSWER_TYPE_PARAGRAPH]["references"].append(decode_unicode(ref_question.get("answer", "")))
                        data[VQA_ANSWER_TYPE_PARAGRAPH]["predictions"].append(decode_unicode(pred_question.get("answer", "")))
                    elif ref_answer_type == VQA_ANSWER_TYPE_LIST:
                        data[VQA_ANSWER_TYPE_LIST]["references"].append(decode_unicode(ref_question.get("answer", "")))
                        data[VQA_ANSWER_TYPE_LIST]["predictions"].append(decode_unicode(pred_question.get("answer", "")))
                    elif ref_answer_type == VQA_ANSWER_TYPE_YESNO:
                        data[VQA_ANSWER_TYPE_YESNO]["references"].append(decode_unicode(ref_question.get("answer", "")))
                        data[VQA_ANSWER_TYPE_YESNO]["predictions"].append(decode_unicode(pred_question.get("answer", "")))


    # Compute metric scores per task
    scores = {}

    if task == "classification":
        # classification
        scores = metric_accuracy_precision_recall_f1(groundtruths=data["references"],
                                                     predictions=data["predictions"],
                                                     labels=CLASSES)
    
    elif task == "summarization":
        scores = compute_paragraph_score(groundtruths=data["references"],
                                         predictions=data["predictions"])

        rouge_avg = (scores["rouge1"] + scores["rouge2"] + scores["rougeL"]) / 3
        scores["weighted_score"] = (0.5 * rouge_avg) + (0.5 * scores["bertscore_f1"])

    elif task == "data_extraction":
        scores = compute_datatable_metrics(groundtruths=data["references"],
                                           predictions=data["predictions"])
        
        scores["weighted_score"] = (0.5 * scores["rms"]) + (0.5 * scores["teds"])

    elif task == "vqa":
        answer_type_weights = {
            "factoid": 0.25,
            "list": 0.25,
            "paragraph": 0.25,
            "yesno": 0.25
        }
   
        scores[VQA_ANSWER_TYPE_FACTOID] = compute_factoid_score(groundtruths=data[VQA_ANSWER_TYPE_FACTOID]["references"], predictions=data[VQA_ANSWER_TYPE_FACTOID]["predictions"])
        scores[VQA_ANSWER_TYPE_PARAGRAPH] = compute_paragraph_score(groundtruths=data[VQA_ANSWER_TYPE_PARAGRAPH]["references"], predictions=data[VQA_ANSWER_TYPE_PARAGRAPH]["predictions"])
        scores[VQA_ANSWER_TYPE_LIST] = compute_list_score(groundtruths=data[VQA_ANSWER_TYPE_LIST]["references"], predictions=data[VQA_ANSWER_TYPE_LIST]["predictions"])
        scores[VQA_ANSWER_TYPE_YESNO] = compute_yesno_score(groundtruths=data[VQA_ANSWER_TYPE_YESNO]["references"], predictions=data[VQA_ANSWER_TYPE_YESNO]["predictions"])
        scores["weighted_score"] = compute_weighted_score(metric_scores=scores,
                                                         answer_type_weights=answer_type_weights)
    
    if task == "vqa":
        scores_temp = scores.copy()
        scores = {
            "factoid_rouge1": scores_temp[VQA_ANSWER_TYPE_FACTOID]["rouge1"],
            "factoid_rouge2": scores_temp[VQA_ANSWER_TYPE_FACTOID]["rouge2"],
            "factoid_rougeL": scores_temp[VQA_ANSWER_TYPE_FACTOID]["rougeL"],
            "factoid_exact_match": scores_temp[VQA_ANSWER_TYPE_FACTOID]["exact_match"],

            "paragraph_rouge1": scores_temp[VQA_ANSWER_TYPE_PARAGRAPH]["rouge1"],
            "paragraph_rouge2": scores_temp[VQA_ANSWER_TYPE_PARAGRAPH]["rouge2"],
            "paragraph_rougeL": scores_temp[VQA_ANSWER_TYPE_PARAGRAPH]["rougeL"],
            "paragraph_bertscore_precision": scores_temp[VQA_ANSWER_TYPE_PARAGRAPH]["bertscore_precision"],
            "paragraph_bertscore_recall": scores_temp[VQA_ANSWER_TYPE_PARAGRAPH]["bertscore_recall"],
            "paragraph_bertscore_f1": scores_temp[VQA_ANSWER_TYPE_PARAGRAPH]["bertscore_f1"],

            "list_set-based-precision": scores_temp[VQA_ANSWER_TYPE_LIST]["set-based-precision"],
            "list_set-based-recall": scores_temp[VQA_ANSWER_TYPE_LIST]["set-based-recall"],
            "list_set-based-f1": scores_temp[VQA_ANSWER_TYPE_LIST]["set-based-f1"],

            "yesno_accuracy": scores_temp[VQA_ANSWER_TYPE_YESNO]["accuracy"],
            "yesno_precision": scores_temp[VQA_ANSWER_TYPE_YESNO]["precision"],
            "yesno_recall": scores_temp[VQA_ANSWER_TYPE_YESNO]["recall"],
            "yesno_f1_score": scores_temp[VQA_ANSWER_TYPE_YESNO]["f1_score"],

            "weighted_score": scores["weighted_score"]
        }


    # Writing scores to JSON
    print('Saving scores to: ', output_scores_path)
    with open(output_scores_path, 'w') as score_file:
        score_file.write(json.dumps(scores))




if __name__ == "__main__":
    try:
        print('\nSci-ImageMiner - Evaluation Script')
        print()

        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
