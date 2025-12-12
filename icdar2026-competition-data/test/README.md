## Test Data

The test data consist of 21 papers.

### 🗂️ Directory Structure

```text
icdar2026-competition-data
├── test
│   ├── main-category
│   │   ├── sub-category
│   │   │   ├── paper #
│   │   │   │   ├── images
│   │   │   │   │   └── figures
│   │   │   │   │      ├── filename.jpg            # (JPEG) actual figure image
│   │   │   │   │      ├── filename.json           # (JSON) figure annotations
│   │   │   │   │      └── ...
│   │   │   │   ├── Author et al.pdf                # (PDF) actual PDF document
│   │   │   │   ├── content.json                    # (JSON) structured content
│   │   │   │   └── ...
│   │   │   └── ...
```

### 📝 Annotations

The figure annotations are distributed and stored alongside each figure in the "images" folder.
Following is the test annotation as JSON format:

```text
root
├── figure_path: Relative path to the figure JPG
├── file_name: Filename of the figure JPG
├── figure_label: Figure label as mentioned in the paper
├── figure_caption: Figure caption as mentioned in the paper
└── boundingBoxes: bounding box coordinates to extract each sub-figure
    └── [0]
        ├── label: (alphabetically labeled for each sub-figure)
        ├── x: x-coordinate
        ├── y: y-coordinate
        ├── width: width of sub-figure
        └── height: height of sub-figure
    ...
```