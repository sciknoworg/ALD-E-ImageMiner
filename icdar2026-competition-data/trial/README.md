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
Following is the general annotation as JSON format:

```text
root
├── figure_path: Relative path to the figure JPG
├── file_name: Filename of the figure JPG
├── figure_label: Figure label as mentioned in the paper
├── figure_caption: Figure caption as mentioned in the paper
├── class: Figure class label (alphabetically labeled for each sub-figure)
├── datatable: Markdown data table (alphabetically labeled for each sub-figure)
├── summary: Figure summary (alphabetically labeled for each sub-figure)
├── q1_type: Either of 4 question types: Process-Oriented, Comparative/Trend, Structure-Property, Application/Performance (alphabetically labeled for each sub-figure)
├── q1: Question text
├── a1_type: Either of 4 answer types: Paragraph, Factoid, List, Yes/No
├── a1: Answer text
├── q2_type: Either of 4 question types: Process-Oriented, Comparative/Trend, Structure-Property, Application/Performance (alphabetically labeled for each sub-figure)
├── q2: Question text
├── a2_type: Either of 4 answer types: Paragraph, Factoid, List, Yes/No
├── a2: Answer text
├── q3_type: Either of 4 question types: Process-Oriented, Comparative/Trend, Structure-Property, Application/Performance (alphabetically labeled for each sub-figure)
├── q3: Question text
├── a3_type: Either of 4 answer types: Paragraph, Factoid, List, Yes/No
├── a3: Answer text
├── q4_type: Either of 4 question types: Process-Oriented, Comparative/Trend, Structure-Property, Application/Performance (alphabetically labeled for each sub-figure)
├── q4: Question text
├── a4_type: Either of 4 answer types: Paragraph, Factoid, List, Yes/No
├── a4: Answer text
└── boundingBoxes: bounding box coordinates to extract each sub-figure
    └── [0]
        ├── label: (alphabetically labeled for each sub-figure)
        ├── x: x-coordinate
        ├── y: y-coordinate
        ├── width: width of sub-figure
        └── height: height of sub-figure
    ...
```
