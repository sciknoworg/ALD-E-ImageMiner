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
- content.json - (JSON) structured content extracted using MinerU
- content.md - (Markdown) structured content extracted using MinerU
- content.tei.xml - (TEI-XML) structured content extracted using GROBID
- content.txt - (Text) unstructured content extracted using MinerU

#### 3. Image
- filename.jpg - (JPEG) actual figure image extracted using MinerU
- filename.class.txt - (Text) chart visualization class/category extracted using Qwen 2.5 VL
- filename.data.txt  - (Text) data extracted as a markdown table extracted using instruction tuned Qwen 2.5 VL
- filename.summary.txt - (Text) summarization of chart visualization extracted using Qwen 2.5 VL

#### 4. Others
- layout.json - (JSON) bounding box and segmentation data containing the PDF layout information extracted using MinerU


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

## 🛠️ Datamining Tools, Libraries and AI Models

### 1. GROBID
GROBID (GeneRation Of BIbliographic Data) is an open-source, machine-learning-based tool designed to parse and extract structured information from scholarly documents, primarily in PDF format. It takes raw, unstructured documents—such as research papers and identifies, tags, and extracts their constituent parts into a standardized TEI XML format. This includes precisely parsing the document's header (title, authors, affiliations, abstract), body text (sections, paragraphs), and, most notably, its citations and bibliography.

URL: [https://github.com/kermitt2/grobid](https://github.com/kermitt2/grobid)

### 2. MinerU
MinerU, created by OpenDataLab, is an open-source tool designed for data extraction from PDF documents, converting them into structured machine-readable formats like Markdown and JSON. MinerU can interpret the complex layout structure of research papers, including figures, tables, formulas, and text.

URL: [https://github.com/opendatalab/MinerU](https://github.com/opendatalab/MinerU)

### 3. Qwen 2.5 VL
Qwen2.5-VL is the open=source multimodal (Vision-Language) version of the Qwen 2.5 series of large language models, also developed by Alibaba. This state-of-the-art model is designed to understand and converse about both text and images simultaneously. It can accept image inputs alongside text prompts and perform a wide range of tasks, including generating detailed descriptions of images, answering questions about visual content (Visual Question Answering), interpreting complex charts and graphs, and engaging in open-ended dialogue about a picture.

URL: [https://github.com/QwenLM/Qwen2.5-VL](https://github.com/QwenLM/Qwen2.5-VL)


### 4. GROBID Python Client
The GROBID Python Client is a software library that provides a convenient Pythonic interface to interact with a GROBID service from within a Python application.

URL: [https://github.com/kermitt2/grobid_client_python](https://github.com/kermitt2/grobid_client_python)
