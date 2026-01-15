## Trial Data

A **trial dataset** is currently available to help participants familiarize themselves with the data format, annotation structure, and figure types used in the competition.

The trial release includes: **one ALD/E research paper**, and its associated **annotated scientific figures**, with a focus on quantitative plots.

### 🗂️ Directory Structure

```text
icdar2026-competition-data
├── trial
│   ├── main-category
│   │   ├── sub-category
│   │   │   ├── paper #
│   │   │   │   ├── images
│   │   │   │   │   ├── filename.jpg            # (JPEG) actual figure image
│   │   │   │   │   ├── filename.json           # (JSON) figure annotations
│   │   │   │   │   └── ...
│   │   │   │   ├── Author et al.pdf                # (PDF) actual PDF document
│   │   │   │   ├── content.json                    # (JSON) structured content
│   │   │   │   └── ...
│   │   │   └── ...
```

### 📝 Annotations

#### Schema

Following is the general top-level schema of each JSON file:

```json
{
    "sample_id": str,
    "classification": dict,
    "summarization": dict,
    "data_extraction": dict,
    "vqa": dict,
    "bbox": dict
}
```

Each "dict" contains alphabetical keys-values pairs to represent each sub-figure task-specific data as shown below:

```json
{
    "sample_id": str,
    "classification": {
        "a": str,
        "b": str,
        ...
    },
    "summarization": {
        "a": str,
        "b": str,
        ...
    },
    "data_extraction": {
        "a": str,
        "b": str,
        ...
    },
    "vqa": {
        "a": list,
        "b": list,
        ...
    },
    "bbox": {
        "a": {
            "x": int,
            "y": int,
            "width": int,
            "height": int
        },
        "b": {
            "x": int,
            "y": int,
            "width": int,
            "height": int
        },
        ...
    },
}
```

Each item in the VQA list should have the following structure:

```json
{
    "question_type": str,
    "questions": str,
    "answer_type": str,
    "answer": str
},
```


#### Description

- **sample_id**: Unique sample id, represents actual path to the figure
- **classification**: Data for the classification task 
- **summarization**: Data for the Summarization task
- **data_extraction**: Data for the Data extraction task
- **vqa**: Data for the VQA task
- **bbox**: Bounding box coordinates to extract each sub-figure
