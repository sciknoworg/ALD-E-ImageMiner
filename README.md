<div align="center">
  <img src="assets/logo-github.png" alt="ALD/E-ImageMiner Logo" width="400"/>
</div>

## Project Overview  

**ALD/E-ImageMiner** is an annotation project on figures from **atomic layer deposition (ALD)** and **atomic layer etching (ALE)**, situated within the broader field of materials science and engineering. Within each of these categories, the data is further organized into the sub-categories **experimental-usecase** and **simulation-usecase**.  

It aims to host gold-standard annotations for chart classification, data extraction, summarization, and question answering—providing both pilot and full-phase data to support multimodal AI research in scientific image understanding.   

### 🗂️ Directory Structure  

We have compiled the dataset for annotation in this repository, structured into clearly defined categories and sub-categories.  
The layout reflects the distinction between ALD and ALE literature, as well as between experimental and simulation studies, making it easier to navigate both the pilot and full annotation phases.  


```text
data
├── pilot-annotation-task
│   ├── atomic-layer-deposition
│   │   ├── experimental-usecase
│   │   │   ├── paper #
│   │   │   │   ├── images
│   │   │   │   │   ├── figures
│   │   │   │   │   │   ├── filename 1.jpg          # (JPEG) actual figure image extracted using MinerU
│   │   │   │   │   │   ├── filename.class.txt      # (Text) chart visualization class/category extracted using Qwen 2.5 VL
│   │   │   │   │   │   ├── filename.data.txt       # (Text) data extracted as a markdown table using instruction-tuned Qwen 2.5 VL
│   │   │   │   │   │   └── filename.summary.txt    # (Text) summarization of chart visualization extracted using Qwen 2.5 VL
│   │   │   │   │   ├── formulas
│   │   │   │   │   │   ├── filename.jpg            # (JPEG) actual formula image extracted using MinerU
│   │   │   │   │   └── tables
│   │   │   │   │       ├── filename.jpg            # (JPEG) actual table image extracted using MinerU
│   │   │   │   ├── Author et al.pdf                # (PDF) actual PDF document
│   │   │   │   ├── content.json                    # (JSON) structured content extracted using MinerU
│   │   │   │   ├── content.md                      # (Markdown) structured content extracted using MinerU
│   │   │   │   ├── content.tei.xml                 # (TEI-XML) structured content extracted using GROBID
│   │   │   │   ├── content.txt                     # (Text) unstructured content extracted using MinerU
│   │   │   │   └── layout.json                     # (JSON) bounding box and segmentation data from MinerU
│   │   │   └── ...
│   │   └── simulation-usecase
│   │       └── ...
│   └── atomic-layer-etching
│       └── ...
└── full-annotation-task
    ├── atomic-layer-deposition
    │   ├── experimental-usecase
    │   └── simulation-usecase
    └── atomic-layer-etching
        ├── experimental-usecase
        └── simulation-usecase
```

## 🛠️ Tools Used

- **[GROBID (GeneRation Of BIbliographic Data)](https://github.com/kermitt2/grobid)** → scholarly PDF parsing into TEI XML.
- **[GROBID Python Client](https://github.com/kermitt2/grobid_client_python)** → Python interface to GROBID.
- **[MinerU](https://github.com/opendatalab/MinerU)** → structured text, figures, formulas, and tables from PDFs. It is created by OpenDataLab as an open-source tool designed for data extraction from PDF documents, converting them into structured machine-readable formats like Markdown and JSON. MinerU can interpret the complex layout structure of research papers, including figures, tables, formulas, and text.
- **[Qwen2.5-VL](https://github.com/QwenLM/Qwen2.5-VL)** → multimodal LLM applied for classification, extraction, and summarization. Specifically, we used [Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct).  
  The [Prompts.md](Prompts.md) file documents the prompts used for information extraction (figure type, data, summary, and figure labels).  


### 📊 Dataset Statistics

#### Overall

| Category | Sub-category | PDFs | Figures | Formulas | Tables |
| --- | --- | --- | --- | --- | --- |
| atomic-layer-deposition | experimental-usecase | 66 | 552 | 102 | 76 |  796 |
| atomic-layer-deposition | simulation-usecase | 58 | 579 | 413 | 131 | 1181 |
| atomic-layer-etching | experimental-usecase | 47 | 461 | 116 | 28 |  652 |
| atomic-layer-etching | simulation-usecase | 32 | 346 | 165 | 55 |  598 |
| **Total** | - | **203** | **1938** | **796** | **290** |

#### Figure type classification

We have defined a taxonomy of 40 figure types including "unknown". The full taxonomy with descriptions, parent taxonomy category, and aliases is here [figure_taxonomy.tsv](https://github.com/sciknoworg/ALD-E-ImageMiner/blob/main/figure_taxonomy.tsv). The ALD/E-ImageMiner project maintains a focus only on figures of parent taxonomy category `quantitative plot`.

Individual statistics for each annotation task dataset distribution are also available i.e. [pilot-annotation-task](pilot-annotation-task/README.md) and [full-annotation-task](full-annotation-task/README.md).

| Figure Type | Auto Labels | Human Labels |
| --- | --- | --- |
| 3d bar chart | 5 | 0 |
| 3d scatter plot | 23 | 0 |
| apparatus diagram | 98 | 0 |
| area chart | 6 | 0 |
| band diagram | 12 | 0 |
| bar chart | 46 | 0 |
| box plot | 4 | 0 |
| bubble chart | 1 | 0 |
| conceptual diagram | 127 | 0 |
| formula | 3 | 0 |
| grouped bar chart | 26 | 0 |
| heatmap | 89 | 0 |
| histogram | 2 | 0 |
| image panel | 526 | 0 |
| line chart | 1066 | 0 |
| line plot | 2 | 0 |
| map/geo chart | 4 | 0 |
| molecular structure diagram | 807 | 0 |
| multi-axis chart | 114 | 0 |
| multiple line chart | 44 | 0 |
| network diagram | 1 | 0 |
| periodic table map | 3 | 0 |
| pie chart | 8 | 0 |
| polar chart | 14 | 0 |
| process flow diagram | 28 | 0 |
| reaction scheme | 443 | 0 |
| scatter plot | 201 | 0 |
| spectra chart | 419 | 0 |
| stacked bar chart | 4 | 0 |
| table | 6 | 0 |
| timeline chart | 6 | 0 |
| unknown | 12 | 0 |
| **Total** | **4150** | **0** |

## 📖 Citation  

The **ALD/E-ImageMiner project vision** is described in the following working paper, pre-released on Zenodo.  
Please cite this paper if you find this work useful:  

```bibtex
@misc{d_souza_2025_17130928,
  author       = {D'Souza, Jennifer},
  title        = {A Pathway to General-Purpose Scientific AI:
                   Multimodal Comprehension of Scientific Images},
  month        = sep,
  year         = 2025,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.17130928},
  url          = {https://doi.org/10.5281/zenodo.17130928},
}
```

## ⭐ Acknowledgements  

The **ALD/E-ImageMiner** project is supported by:  

<img src="https://www.nfdi4datascience.de/images/downloads/Logo_NFDI4DataScience.png" alt="NFDI4DataScience Logo" width="120"/>

- The [NFDI4DataScience](https://www.nfdi4datascience.de/) initiative, funded by the **German Research Foundation (DFG, Grant ID: 460234259)**, under the *Speedboat Annotation Project* funding scheme.  


- The *AI-Aware Pathways to Sustainable Semiconductor Process and Manufacturing Technologies (AWASES)* initiative (Mackus et al., 2024), funded by **Merck and Intel**, with collaboration between **Eindhoven University**, **Leibniz University Hannover’s L3S Research Centre (co-led by applicants)**, and **University of Warwick**. AWASES hosts three fully funded PhD positions and supports advances in **generative AI, multimodal models, and FAIR scientific knowledge graph construction**.  

