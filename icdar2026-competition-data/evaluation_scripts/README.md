# 📊 Sci-ImageMiner Evaluation Script

This README provides instructions and information regarding the evaluation script used for the Sci-ImageMiner ICDAR 2026 competition. The evaluation script is used during the competition development and evaluation phase for scoring submissions. The scripts requires to use consolidated predictions in [JSON format](https://github.com/sciknoworg/ALD-E-ImageMiner/tree/main/icdar2026-competition-data/test/submission_guidelines) for each task, which will be evaluated based on per task [evaluation metrics](https://sites.google.com/view/sci-imageminer/task-evaluation-metrics).


## ℹ️ Command-line arguments

The script requires four user inputs:

- **task**: Task to evaluate (e.g. classification, data extraction, summarization, vqa)
- **reference-path**: Path to reference JSON file
- **prediction-path**: Path to prediction JSON file
- **output-scores-path**: Path to output scores JSON file


## ⚙️ Installation

The required Python packages needs to be installed before you can use the script:

```bash
pip install -r requirements.txt
```

## 💻 Usage

### Run Evaluation

```bash
python sci-imageminer_evaluation.py
    --task classification
    --reference-path reference_data.json
    --prediction-path prediction_data.json
    --output-scores-path scores_cls.json
```

### Example Output

```bash
Sci-ImageMiner - Evaluation Script

Task: classification
Reference path: reference_data.json
Prediction path: prediction_data.json
Output path: scores_cls.json

Saving scores to:  scores_cls.json
```


## 📄 License
The code is released under [CC by 4.0](license.txt).


