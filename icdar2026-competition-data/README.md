<div align="center">
  <img src="assets/logo-github.png" alt="ALD/E-ImageMiner Logo" width="400"/>
</div>

# ICDAR 2026 Competition
## Sci-ImageMiner - Information Extraction from Atomic Layer Deposition/Etching (ALD/E) Scientific Figures

📄🔬📊🧪

Welcome to the official GitHub repository for the **ICDAR 2026 Competition on Information Extraction from Atomic Layer Deposition/Etching (ALD/E) Scientific Figures (Sci-ImageMiner)**.

This repository provides data formats, datasets and instructions for using the dataset and preparing submissions.

### 🌍 Competition Website
https://sites.google.com/view/sci-imageminer

### 💡 About

The **Sci-ImageMiner** competition defines four complementary tasks that evaluate multimodal understanding of scientific figures in Atomic Layer Deposition and Etching (ALD/E) research.

- **Task 1** - targets chart-type **classification**
- **Task 2** - focuses on **data table extraction** from plots
- **Task 3** - assesses **summarization** of key scientific insights conveyed by figures.
- **Task 4** - introduces **visual question-answering** across four scientific reasoning sub-tasks, requiring systems to interpret complex visual and textual elements.

Together, these tasks provide a comprehensive benchmark for visual scientific reasoning in a highly specialized domain. 

### 📂 Directory Structure

In general, all the dataset splits follow the same directory structure as shown below:

```text
icdar2026-competition-data
├── dataset-split
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

## 🗂️ Datasets

The full competition dataset will be released **in batches according to the competition timeline**, including: training & development data, and a final blind test set.

The information for the ICDAR 2026 competition for each dataset split is following:

1. [Trial Dataset](trial/)

2. [Training Dataset](train/)

3. [Development/validation Dataset](dev/)

4. [Test Dataset](test/)

## ⚙️ Evaluation Scripts

The [evaluation scripts](evaluation_scripts/) are released which have been used for the Sci-ImageMiner ICDAR 2026 competition.

## 📧 Contact & Support

**Email:** sciknoworg [at] gmail.com

#### Discussions / issues:

**Google Groups:** https://groups.google.com/u/4/g/sci-imageminer/

**Email:** sci-imageminer [at] googlegroups.com







