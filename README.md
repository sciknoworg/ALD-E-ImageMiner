<div align="center">
  <img src="assets/logo-github.png" alt="ALD/E-ImageMiner Logo" width="400"/>
</div>

<p align="center">
  <a href="https://huggingface.co/datasets/SciKnowOrg/ALD-E-ImageMiner">
    <img alt="Hugging Face Dataset" src="https://img.shields.io/badge/Hugging%20Face-Dataset-FFD21E?style=for-the-badge">
  </a>
  <a href="https://sites.google.com/view/sci-imageminer/">
    <img alt="Competition Website" src="https://img.shields.io/badge/Competition-Website-4285F4?style=for-the-badge">
  </a>
  <a href="https://sciknoworg.github.io/ALD-E-ImageMiner/">
    <img alt="Paper Page" src="https://img.shields.io/badge/Paper-Page-087F83?style=for-the-badge">
  </a>
  <a href="https://arxiv.org/abs/2607.26848">
    <img alt="arXiv 2607.26848" src="https://img.shields.io/badge/arXiv-2607.26848-B31B1B?style=for-the-badge">
  </a>
</p>

## Project Overview

**ALD/E-ImageMiner** is an expert-annotated benchmark for scientific figure understanding in **atomic layer deposition (ALD)** and **atomic layer etching (ALE)** literature. The data is organized by process domain, by source-paper use case (**experimental-usecase** or **simulation-usecase**), and by competition split.

The benchmark supports four information-extraction tasks:

- **Figure type classification**
- **Data table extraction**
- **Figure summarization**
- **Visual question answering**

The current GitHub release is centered on figure images and their JSON annotations. Source article PDFs are intentionally excluded from GitHub distribution.

### 🗂️ Directory Structure

```text
icdar2026-competition-data/
├── train/
│   └── <main-category>/
│       └── <sub-category>/
│           └── <paper-id>/
│               ├── images/
│               │   ├── <figure-id>.jpg
│               │   └── <figure-id>.json
│               └── content.json
├── dev/
│   └── ...
├── test/
│   ├── gold_standard_test_set/
│   │   └── ...
│   ├── blind_test_set/
│   │   └── ...
│   └── submission_guidelines/
└── evaluation_scripts/
```

The main categories are:

- `atomic-layer-deposition`
- `atomic-layer-etching`

The sub-categories are:

- `experimental-usecase`
- `simulation-usecase`

Each figure annotation JSON contains `sample_id`, `classification`, and `bbox`. Many records also include `summarization`, `data_extraction`, and `vqa`. Source paper PDFs may exist in local working copies, but they are not part of the GitHub release and are ignored by Git.

## 🛠️ Tools Used In Data Preparation

The current public release includes image files, annotation JSON files, and structured `content.json` files. The tools relevant to these released artifacts are:

- **[MinerU](https://github.com/opendatalab/MinerU)**: used during preparation to extract structured content and figure images from source PDFs.
- **[Qwen2.5-VL](https://github.com/QwenLM/Qwen2.5-VL)**: used in the prompt workflow documented in [Prompts.md](Prompts.md) for machine-assisted figure understanding tasks such as figure type, data extraction, summarization, and figure labels.
- **[ORKG Image Annotation](https://orkg.org/image-annotation/)**: expert annotation workflow used to produce and review the released benchmark annotations. Please contact the project team for access.

Older README references to GROBID/TEI XML artifacts have been removed from this release description because no `content.tei.xml` files are included in the current repository snapshot.

## Figure Taxonomy

![A visualization of scientific figure taxonomy](figure_taxonomy.png)

The taxonomy file [figure_taxonomy.tsv](figure_taxonomy.tsv) currently lists **49** figure types, including `unknown`. The train/dev/gold-standard-test annotations contain **37 observed** figure-type labels. The taxonomy covers quantitative plots, scientific schematics, domain-specific scientific image panels, matrix layouts, and other figure forms.

## 📊 Dataset Statistics

The statistics below are computed from annotation JSON files in:

- `icdar2026-competition-data/train`
- `icdar2026-competition-data/dev`
- `icdar2026-competition-data/test/gold_standard_test_set`

Paper counts mean paper directories that contain figure annotations. Figure counts mean annotated full-figure image records.

| Split | ALD exp. papers | ALD exp. figures | ALD sim. papers | ALD sim. figures | ALE exp. papers | ALE exp. figures | ALE sim. papers | ALE sim. figures | Total papers | Total figures |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Train | 42 | 330 | 35 | 349 | 27 | 248 | 22 | 243 | 126 | 1170 |
| Dev | 6 | 50 | 6 | 59 | 5 | 55 | 3 | 37 | 20 | 201 |
| Test | 18 | 172 | 17 | 149 | 14 | 138 | 10 | 121 | 59 | 580 |
| **Total** | **66** | **552** | **58** | **557** | **46** | **441** | **35** | **401** | **205** | **1951** |

The public gold-standard totals above exclude `test/blind_test_set` and `test/submission_guidelines`.

### Figure Type Classification By Split

Classification counts are panel-level annotation entries. A single full-figure image can contain multiple labeled panels and therefore can contribute more than one classification entry.

| Figure type | Train | Dev | Test | Total |
|---|---:|---:|---:|---:|
| molecular structure diagram | 388 | 101 | 245 | 734 |
| multiple line chart | 263 | 49 | 131 | 443 |
| image panel | 235 | 33 | 86 | 354 |
| multiple scatter plot | 176 | 15 | 74 | 265 |
| multi spectra chart | 153 | 10 | 94 | 257 |
| conceptual diagram | 146 | 35 | 45 | 226 |
| scatter plot | 133 | 16 | 63 | 212 |
| reaction scheme | 130 | 32 | 43 | 205 |
| line chart | 114 | 29 | 51 | 194 |
| stacked spectra chart | 114 | 7 | 37 | 158 |
| multi-axis chart | 82 | 5 | 47 | 134 |
| spectra chart | 74 | 2 | 42 | 118 |
| heatmap | 75 | 0 | 28 | 103 |
| reaction energy profile diagram | 61 | 0 | 24 | 85 |
| apparatus diagram | 51 | 1 | 28 | 80 |
| process flow diagram | 43 | 2 | 9 | 54 |
| bar chart | 35 | 2 | 13 | 50 |
| unknown | 29 | 7 | 11 | 47 |
| contour heatmap | 38 | 0 | 8 | 46 |
| process timing diagram | 16 | 12 | 11 | 39 |
| device structure diagram | 10 | 2 | 4 | 16 |
| 3d scatter plot | 10 | 0 | 4 | 14 |
| band diagram | 5 | 0 | 8 | 13 |
| grouped bar chart | 9 | 0 | 3 | 12 |
| box plot | 6 | 0 | 4 | 10 |
| phase diagram | 4 | 0 | 3 | 7 |
| stacked bar chart | 7 | 0 | 0 | 7 |
| workflow diagram | 6 | 0 | 1 | 7 |
| pie chart | 4 | 0 | 0 | 4 |
| periodic table map | 1 | 0 | 2 | 3 |
| table | 3 | 0 | 0 | 3 |
| timeline chart | 1 | 2 | 0 | 3 |
| formula | 2 | 0 | 0 | 2 |
| network diagram | 0 | 0 | 2 | 2 |
| polar chart (rose chart) | 2 | 0 | 0 | 2 |
| area chart | 1 | 0 | 0 | 1 |
| chromaticity diagram | 1 | 0 | 0 | 1 |
| **Total** | **2428** | **362** | **1121** | **3911** |

## ⚖️ License And Reuse

This repository is a **mixed-rights, non-commercial benchmark resource**. It contains CC BY 4.0 annotations and generated metadata, plus extracted scientific figure images derived from many source articles. There is no blanket open license for all images or source-paper content.

Source article PDFs are intentionally excluded from GitHub distribution. This release is intended for non-commercial research, benchmarking, and evaluation use. Before reusing, redistributing, or commercially using any image, users must check the corresponding source article and rights holder terms. Where individual files or subdirectories include their own license notices, those notices apply to those files.

The granularity is record/image-level rather than corpus-level: annotations and generated metadata are released as `CC BY 4.0`; each extracted figure image and source-derived paper field follows the rights and reuse terms of its corresponding source article. This is consistent with the Hugging Face package, which is marked as `license: other` / `license_name: mixed-rights-non-commercial` and exposes per-record fields such as `metadata_license: CC BY 4.0`, `image_license: source_publisher_rights_reserved`, and `image_reuse_status: non_commercial_research_use_only`.

See [LICENSE](LICENSE) for the repository-level mixed-rights notice.

## 📖 Citation

The vision working paper for this project is pre-released on Zenodo. Please cite this paper if you find the project useful:

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

This benchmark dataset was used as the **[ICDAR 2026 Competition on Information Extraction from Atomic Layer Deposition/Etching (ALD/E) Scientific Figures](https://sites.google.com/view/sci-imageminer/)**, organized as part of the [ICDAR 2026 competitions](https://icdar2026.org/index.php/competitions/). Please cite the competition report when referring to the ALD/E-ImageMiner benchmark, dataset, competition, or associated information-extraction tasks:

```bibtex
@article{ahmed2026icdar,
  title   = {ICDAR 2026 Competition on Information Extraction from
             Atomic Layer Deposition/Etching (ALD/E) Scientific Figures},
  author  = {Ahmed, Fahad and Auer, S{\"o}ren and D'Souza, Jennifer},
  journal = {arXiv preprint arXiv:2607.26848},
  year    = {2026},
  url     = {https://arxiv.org/abs/2607.26848}
}
```

## ⭐ Acknowledgements

The development of the **expert-annotated ALD/E-ImageMiner benchmark resource** was funded by:

- <img src="assets/nfdi4ds-logo.png" alt="NFDI4DataScience Logo" width="200" align="middle"/>

  The [NFDI4DataScience](https://www.nfdi4datascience.de/) initiative, funded by the **German Research Foundation (DFG, Grant ID: 460234259)** under the *[Speedboat Annotation Project](https://www.nfdi4datascience.de/community/speed-boat-projects/)* funding scheme.

This research endeavor is conducted in the context of the following project:

- The *AI-Aware Pathways to Sustainable Semiconductor Process and Manufacturing Technologies (AWASES)* initiative (Mackus et al., 2024), funded by **Merck and Intel**, with collaboration between **Eindhoven University**, **Leibniz University Hannover's L3S Research Centre**, and **University of Warwick**. AWASES hosts three fully funded PhD positions and supports advances in **generative AI, multimodal models, and FAIR scientific knowledge graph construction**.
