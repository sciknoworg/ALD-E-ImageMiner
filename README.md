## 📋 ALD-E-ImageMiner Overview


## Dataset

### Organization

#### Categories

- atomic-layer-deposition
- atomic-layer-etching

#### Sub-categories

- experimental-usecase
- simulation-usecase

### 🗂️ Directory Structure
```text
data
├── atomic-layer-deposition
│   ├── experimental-usecase
│   │   ├── 1
│   │   │   ├── images
│   │   │   │   ├── figures
│   │   │   │   │   ├── filename.jpg
│   │   │   │   │   ├── filename.class.txt
│   │   │   │   │   ├── filename.data.txt 
│   │   │   │   │   └── filename.summary.txt
│   │   │   │   ├── formulas
│   │   │   │   │   ├── filename.jpg
│   │   │   │   │   ├── filename.class.txt
│   │   │   │   │   ├── filename.data.txt 
│   │   │   │   │   └── filename.summary.txt
│   │   │   │   └── tables
│   │   │   │       ├── filename.jpg
│   │   │   │       ├── filename.class.txt
│   │   │   │       ├── filename.data.txt 
│   │   │   │       └── filename.summary.txt
│   │   │   ├── Author et al.pdf
│   │   │   ├── content.json
│   │   │   ├── content.md
│   │   │   ├── content.tei.xml
│   │   │   ├── content.txt
│   │   │   └── layout.json
...
│   │   └── N
│   │       ├── image
│   │       │   ├── figures
│   │       │   ├── formulas
│   │       │   └── tables
│   │       ├── Author et al.pdf
│   │       ├── content.json
│   │       ├── content.md
│   │       ├── content.tei.xml
│   │       ├── content.txt
│   │       └── layout.json
│   └── simulation-usecase
└── atomic-layer-etching
    ├── experimental-usecase
    └── simulation-usecase
```

### File Descriptions
#### 1. PDF
- Author et al.pdf - (PDF) actual PDF document

#### 2. Text
- content.json - (JSON) structured content
- content.md - (Markdown) structured content
- content.tei.xml - (TEI-XML) structured content
- content.txt - (Text) unstructured content

#### 3. Image
- filename.jpg - (JPEG) actual figure image
- filename.class.txt - (Text) chart visualization class/category
- filename.data.txt  - (Text) data extracted as a markdown table
- filename.summary.txt - (Text) summarization of chart visualization

#### 4. Others
- layout.json - (JSON) bounding box and segmentation data containing the PDF layout information


### 📊 Statistics

#### Overall Statistics

| Category | Sub-category | PDFs | Figures | Formulas | Tables |
| --- | --- | --- | --- | --- | --- |
| atomic-layer-deposition | experimental-usecase | 66 | 552 | 102 | 76 |  796 |
| atomic-layer-deposition | simulation-usecase | 58 | 579 | 413 | 131 | 1181 |
| atomic-layer-etching | experimental-usecase | 47 | 461 | 116 | 28 |  652 |
| atomic-layer-etching | simulation-usecase | 32 | 346 | 165 | 55 |  598 |
| **Total** | - | **203** | **1938** | **796** | **290** |

#### Figure type classification

| Chart Type | Auto Labels | Human Labels |
| --- | --- | --- |
| Area chart | 0 | 0 |
| Bar chart | 13 | 0 |
| 3D bar chart | 18 | 0 |
| Grouped bar chart | 46 | 0 |
| Stacked bar chart | 7 | 0 |
| Box plot | 1 | 0 |
| Bubble chart | 6 | 0 |
| Donut chart | 2 | 0 |
| Funnel chart | 0 | 0 |
| Heatmap | 36 | 0 |
| Line chart | 360 | 0 |
| Multiple Line chart | 580 | 0 |
| Multi-axis chart | 197 | 0 |
| Pie chart | 5 | 0 |
| Polar chart | 9 | 0 |
| Radar chart | 1 | 0 |
| Rose chart | 0 | 0 |
| 3D scatter plot | 1 | 0 |
| Scatter plot | 91 | 0 |
| Treemap | 0 | 0 |
| Unknown | 546 | 0 |
| --- | --- | --- |
| flowchart | 2 | 0 |
| table | 1 | 0 |
| | 15 | 0 |
| ['scatter plot', 'line chart'] | 1 | 0 |
| **Total** | **1938** | **0** |

## 🛠️ Datamining Tools

### MinerU
[MinerU](https://mineru.net/) was used to extract JSON, figures, formulas and tables.


### GROBID
[GROBID](https://github.com/kermitt2/grobid) was used to extract TEI-XML data.

### GROBID Python Client
[GROBID Python client](https://github.com/kermitt2/grobid_client_python) was used as a REST-API client in Python.


