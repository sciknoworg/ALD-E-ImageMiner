# Submission Guidelines

This document describes the required prediction and submission formats for all tasks in the **Sci-ImageMiner** competition.

Participants must strictly follow the specified formats to ensure correct and fair evaluation. Submissions that do not conform to these guidelines may be rejected or scored incorrectly.

All submissions must be provided in **JSON format** and named as "prediction_data.json", compressed as a **ZIP** file and then uploaded via the official **CodaBench** competition platform.

---

## 1. Classification Task

The classification task requires participants to predict the **figure type** for each figure/sub-figure(s).

### Submission Format

The submission must be a JSON array containing one entry per test sample:

```json
[
  {
    "sample_id": "...",
    "classification": { ... }
  },
  {
    "sample_id": "...",
    "classification": { ... }
  },
  ...
]
```

- sample_id: Unique identifier corresponding to a test sample.
- classification: A mapping from figure labels to predicted class names.

### Example

```json
{
  "sample_id": "atomic-layer-etching/experimental-usecase/16/fig_2",
  "classification": {
    "a": "multiple line chart",
    "b": "spectra chart"
  }
}
```

### Additional Resources

- [Sample Submission](sample_submissions/classification/prediction_data.json)
- [Competition Page](https://www.codabench.org/competitions/12901/)

---

## 2. Data Extraction Task

The data extraction task requires extraction underlying quantitative-plot data into structured Markdown tables (GitHub compatible), for each sub-figure.

### Submission Format

The submission must be a JSON array containing one entry per test sample:

```json
[
  {
    "sample_id": "...",
    "data_extraction": { ... }
  },
  {
    "sample_id": "...",
    "data_extraction": { ... }
  },
  ...
]
```

- sample_id: Unique identifier corresponding to a test sample.
- data_extraction: A mapping from figure labels to predicted markdown tables.

Please note:  
- Tables must follow standard GitHub Markdown syntax and enclosed between **\```markdown** and **\```** markers.
- Empty tables are allowed when no extractable data is present.

### Example

```json
{
  "sample_id": "atomic-layer-deposition/experimental-usecase/45/fig_3",
  "data_extraction": {
    "a": "```markdown\n| Temperature (°C) | Growth Rate (Å/cycle) |\n| --- | --- |\n| 200 | 0.85 |\n| 250 | 1.10 |\n```"
  }
}
```

### Additional Resources

- [Sample Submission](sample_submissions/data_extraction/prediction_data.json)
- [Competition Page](https://www.codabench.org/competitions/12902/)

---

## 3. Summarization Task

The summarization task requires generating concise, sub-figure level textual summaries describing the content of each sub-figure.

### Submission Format

The submission must be a JSON array containing one entry per test sample:

```json
[
  {
    "sample_id": "...",
    "summarization": { ... }
  },
  {
    "sample_id": "...",
    "summarization": { ... }
  },
  ...
]
```

- sample_id: Unique identifier corresponding to a test sample.
- summarization: A mapping from figure labels to predicted summaries.

### Example

```json
{
  "sample_id": "atomic-layer-deposition/experimental-usecase/12/fig_1",
  "summarization": {
    "a": "The figure shows the deposition rate as a function of temperature.",
    "b": "The panel illustrates film thickness variation over time."
  }
}
```

### Additional Resources

- [Sample Submission](sample_submissions/summarization/prediction_data.json)
- Competition Page (TBA)

---

## 4. Visual Question Answering (VQA) Task

The VQA task requires answering scientific questions grounded in figure content.
Questions are grouped by sub-figure label and include multiple question and answer types.

### Submission Format

The submission must be a JSON array containing one entry per test sample:

```json
[
  {
    "sample_id": "...",
    "vqa": { ... }
  },
  {
    "sample_id": "...",
    "vqa": { ... }
  },
  ...
]
```

- question_type: Process-Oriented, Comparative/Trend, Structure-Property, Application/Performance
- answer_type: Factoid, List, Paragraph, Yes/No

### Example

```json
{
  "sample_id": "atomic-layer-etching/experimental-usecase/16/fig_2",
  "vqa": {
    "a": [
      {
        "question_type": "Structure-Property",
        "question": "Which materials are etched at CF4 concentrations above 10%?",
        "answer_type": "Factoid",
        "answer": "TiN and SiO2"
      }
    ],
    "b": [
      {
        "question_type": "Comparative/Trend",
        "question": "Does the etch rate increase with RF power?",
        "answer_type": "Yes/No",
        "answer": "Yes"
      }
    ]
  }
}
```

Please note:
- Multiple Q&A pairs per sub-figure are allowed.

### Additional Resources

- [Sample Submission](sample_submissions/vqa/prediction_data.json)
- Competition Page (TBA)

---

## General Notes

- Each submission file must be a single **JSON** file.
- Each **sample_id** must appear at most once per submission sample.
- For each sample, predictions must be provided **at the sub-figure level**, where each sub-figure is identified by a lowercase alphabetical label (e.g., `a`, `b`, `c`).
- Predictions must correspond exactly to the provided test samples.
- Text outputs are evaluated using automatic metrics and are subject to normalization.
- Failure to comply with these formats may result in incorrect scoring or disqualification.

