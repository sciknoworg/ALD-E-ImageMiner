<div align="center">
  <img src="assets/logo-github.png" alt="ALD/E-ImageMiner Logo" width="400"/>
</div>

# ICDAR 2026 Competition: Sci-ImageMiner
## Information Extraction from ALD/E Scientific Figures

📄🔬📊🧪

Welcome to the official GitHub repository for the ICDAR 2026 Competition on Information Extraction from ALD/E Scientific Figures (Sci-ImageMiner).

This repo provides data formats, datasets and instructions for using the dataset and preparing submissions.

### Competition Website
https://sites.google.com/view/sci-imageminer/home?authuser=0

### 🗂️ Directory Structure

In general, all the dataset splits follow the same directory structure as shown below:

```text
icdar2026-competition-data
├── dataset-split
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

### 📝 Annotation Formats
#### 1️⃣ Train / Dev (Val) / Trial Annotation Format

The figure annotations are distributed and stored alongside each figure in the "images" folder for each paper.
Following is the general hierarchy for the annotation JSON format:


```text
root
├── 
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

#### 2️⃣ Test Set Annotation Format

```text
root
├── 
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


## 🗂️ Datasets

The information for the ICDAR 2026 competition for each dataset split is following:

1. [Trial Dataset](trial/)

2. Training Dataset (Coming soon)

3. Development/validation Dataset (Coming soon)

4. Test Dataset (Coming soon)

## 📧 Contact & Support

Email: sciknoworg [at] gmail.com

**Discussions / issues:**
Google Groups: https://groups.google.com/u/4/g/sci-imageminer/
Email: sci-imageminer [at] googlegroups.com







