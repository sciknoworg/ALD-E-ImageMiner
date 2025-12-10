## Test Data

The training data consist of 21 papers.

### 🗂️ Directory Structure

```text
icdar2026-competition-data
├── test
│   ├── main-category
│   │   ├── sub-category
│   │   │   ├── paper #
│   │   │   │   ├── images
│   │   │   │   │   └── figures
│   │   │   │   │      ├── filename 1.jpg          # (JPEG) actual figure image
│   │   │   │   │      └── ...
│   │   │   │   ├── Author et al.pdf                # (PDF) actual PDF document
│   │   │   │   ├── content.json                    # (JSON) structured content
│   │   │   │   ├── content.md                      # (Markdown) structured content
│   │   │   │   ├── content.tei.xml                 # (TEI-XML) structured content
│   │   │   │   └── ...
│   │   │   └── ...
```

### 📝 Anntotions

Following are the details of the annotations in JSON format:

```text
root
├── [0]
│   ├── dataset_main_category: Either "atomic-layer-etching" or "atomic-layer-deposition"
│   ├── dataset_sub_category: Either "experimental-usecase" or "simulation-usecase"
│   ├── dataset_folder_name: A serial number of the paper
│   ├── pdf_path: Relative path to the PDF folder
│   ├── file_name: Filename of the paper PDF
│   └── figure_annotations
│   │   └── figure[0]
│   │       ├── figure_path: Relative path to the figure JPG
│   │       ├── file_name: Filename of the figure JPG
│   │       ├── figure_label: Figure label as mentioned in the paper
│   │       ├── figure_caption: Figure caption as mentioned in the paper
│   │       ├── class: Figure class label (alphabetically labeled for each sub-figure)
│   │       ├── datatable: Markdown data table (alphabetically labeled for each sub-figure)
│   │       ├── summary: Figure summary (alphabetically labeled for each sub-figure)
│   │       ├── q1_type: Either of 4 question types: Process-Oriented, Comparative/Trend, Structure-Property, Application/Performance (alphabetically labeled for each sub-figure)
│   │       ├── q1: Question text
│   │       ├── a1_type: Either of 4 answer types: Paragraph, Factoid, List, Yes/No
│   │       ├── a1: Answer text
│   │       ├── q2_type: Either of 4 question types: Process-Oriented, Comparative/Trend, Structure-Property, Application/Performance (alphabetically labeled for each sub-figure)
│   │       ├── q2: Question text
│   │       ├── a2_type: Either of 4 answer types: Paragraph, Factoid, List, Yes/No
│   │       ├── a2: Answer text
│   │       ├── q3_type: Either of 4 question types: Process-Oriented, Comparative/Trend, Structure-Property, Application/Performance (alphabetically labeled for each sub-figure)
│   │       ├── q3: Question text
│   │       ├── a3_type: Either of 4 answer types: Paragraph, Factoid, List, Yes/No
│   │       ├── a3: Answer text
│   │       ├── q4_type: Either of 4 question types: Process-Oriented, Comparative/Trend, Structure-Property, Application/Performance (alphabetically labeled for each sub-figure)
│   │       ├── q4: Question text
│   │       ├── a4_type: Either of 4 answer types: Paragraph, Factoid, List, Yes/No
│   │       ├── a4: Answer text
│   │       └── boundingBoxes: bounding box coordinates for each sub-figure
│   │           └── [0]
│   │               ├── label: (alphabetically labeled for each sub-figure)
│   │               ├── x: x-coordinate
│   │               ├── y: y-coordinate
│   │               ├── width: width of sub-figure
│   │               └── height: height of sub-figure
│   │               ...
│   │
│   └── ...

```
