## Test Data

The full competition dataset will be released **in batches according to the competition timeline**.

Each release will be announced via the Sci-ImageMiner [Google Group](https://groups.google.com/u/4/g/sci-imageminer/) and reflected on the [Important Dates page](https://sites.google.com/view/sci-imageminer/important-dates).

For task definitions and evaluation details, please refer to the [Task Description](https://sites.google.com/view/sci-imageminer/task-description) and [Task Evaluation Metrics](https://sites.google.com/view/sci-imageminer/task-evaluation-metrics) pages.


### 🗂️ Directory Structure

```text
icdar2026-competition-data
├── test
│   ├── practice-phase
│   │   ├── main-category
│   │   │   ├── sub-category
│   │   │   │   ├── paper #
│   │   │   │   │   ├── images
│   │   │   │   │   │   ├── filename.jpg            # (JPEG) actual figure image
│   │   │   │   │   │   ├── filename.json           # (JSON) figure annotations
│   │   │   │   │   │   └── ...
│   │   │   │   │   ├── Author et al.pdf                # (PDF) actual PDF document
│   │   │   │   │   ├── content.json                    # (JSON) structured content
│   │   │   │   │   └── ...
│   │   │   │   └── ...
│   ├── remaining-test-data
│   │   ├── main-category
│   │   │   ├── sub-category
│   │   │   │   ├── paper #
│   │   │   │   │   ├── images
│   │   │   │   │   │   ├── filename.jpg            # (JPEG) actual figure image
│   │   │   │   │   │   ├── filename.json           # (JSON) figure annotations
│   │   │   │   │   │   └── ...
│   │   │   │   │   ├── Author et al.pdf                # (PDF) actual PDF document
│   │   │   │   │   ├── content.json                    # (JSON) structured content
│   │   │   │   │   └── ...
│   │   │   │   └── ...
```

## Dataset Distribution Statistics

The following summarizes the distribution of **papers** and **figures** by each main and sub-categories in the dataset.

## atomic-layer-deposition

| Sub-category | PDF files | JPG files |
|-------------|-----------|-----------|
| experimental-usecase | 18 | 172 |
| simulation-usecase   | 17 | 149 |
|        Total         | 35 | 321 |

## atomic-layer-etching

| Sub-category | PDF files | JPG files |
|-------------|-----------|-----------|
| experimental-usecase | 14 | 138 |
| simulation-usecase   | 10 | 121 |
|        Total         | 24 | 259 |

### 📝 Annotations

#### Schema

Following is the general top-level schema of each JSON file:

```json
{
    "sample_id": str,
    "bbox": dict
}
```

Each "dict" contains alphabetical keys-values pairs to represent each sub-figure task-specific data as shown below:

```json
{
    "sample_id": str,
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

#### Description

- **sample_id**: Unique sample id, represents actual path to the figure
- **bbox**: Bounding box coordinates to extract each sub-figure
