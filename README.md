# Exoplanet Detection AI

An AI/ML project for detecting exoplanets from stellar light curves using data from the Kepler Space Telescope.

The objective is to identify subtle transit patterns in noisy astronomical observations and build machine learning models capable of distinguishing stars that host exoplanets from those that do not.

---

## Project Structure

```text
exoplanet-detection-ai/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_dataset_exploration.ipynb
│   └── 03_signal_analysis.ipynb
│
├── src/
│   ├── preprocessing/
│   ├── visualization/
│   └── features/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Dataset

This project uses the publicly available Kepler Exoplanet dataset.

Due to GitHub file size limitations, the dataset is not included in this repository.

Place the dataset files inside:

```text
data/raw/
```

Expected files:

```text
exoTrain.csv
exoTest.csv
```

---

## Setup

Clone the repository:

```bash
git clone https://github.com/Aniruddha072/exoplanet-detection-ai.git
cd exoplanet-detection-ai
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open the notebooks directory and run the notebooks in sequence:

1. `01_dataset_exploration.ipynb`
2. `03_signal_analysis.ipynb`

---

## Current Progress

### Completed

- Dataset exploration and inspection
- Data preprocessing and normalization
- Exploratory signal analysis
- Positive vs negative light curve comparison
- Average light curve analysis
- Variability analysis
- PCA-based visualization

### Next Steps

- Statistical feature extraction
- Frequency-domain analysis
- Machine learning model development
- Model evaluation and comparison

---

## Objectives

- Analyze stellar light curves
- Detect exoplanet transit patterns
- Engineer informative signal features
- Train and evaluate classification models
- Improve detection performance on highly imbalanced data

---
