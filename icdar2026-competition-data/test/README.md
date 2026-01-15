## Test Data

The full competition dataset will be released **in batches according to the competition timeline**.

### 🗂️ Directory Structure

```text
icdar2026-competition-data
├── test
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
