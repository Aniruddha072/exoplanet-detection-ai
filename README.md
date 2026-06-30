# Exoplanet Detection AI

An AI-powered system for detecting exoplanets from noisy astronomical light curve data.

This project explores machine learning techniques for identifying exoplanet transit signals from stellar brightness measurements.

---

## Project Structure

```text
exoplanet-detection-ai/
│
├── data/
│   ├── raw/                # Original dataset (not tracked by Git)
│   └── processed/          # Processed datasets (not tracked by Git)
│
├── notebooks/
│   ├── 01_positive_samples.ipynb
│   └── 02_preprocessing.ipynb
│
├── src/
│   └── visualization/
│       └── lightcurve_plots.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Dataset

Dataset used:

- Kepler Exoplanet Search Dataset
- Training Set: 5,087 stars
- Test Set: 570 stars
- Features: 3,197 flux measurements per star

Labels:

| Original | Meaning |
|-----------|----------|
| 1 | No Exoplanet |
| 2 | Exoplanet |

After preprocessing:

| Converted | Meaning |
|-----------|----------|
| 0 | No Exoplanet |
| 1 | Exoplanet |

---

## Progress

### Phase 1 — Data Exploration ✅

- Loaded train and test datasets
- Inspected dataset structure
- Visualized positive samples
- Identified extreme flux outliers
- Investigated class imbalance

### Phase 2 — Data Preprocessing ✅

- Separated features and labels
- Converted labels to binary
- Investigated outliers
- Applied feature standardization
- Compared signals before and after scaling
- Saved processed datasets

### Upcoming Phases

- Exploratory Signal Analysis
- Feature Engineering
- Classical Machine Learning Models
- Deep Learning Models
- Model Evaluation & Comparison

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Aniruddha072/exoplanet-detection-ai.git

cd exoplanet-detection-ai
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

### Windows

```bash
.\.venv\Scripts\activate
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

Open:

```text
notebooks/01_positive_samples.ipynb
```

or

```text
notebooks/02_preprocessing.ipynb
```

and run the cells sequentially.

---

## Notes

Large datasets and processed files are excluded from Git tracking using `.gitignore`.

Expected data location:

```text
data/
├── raw/
│   ├── exoTrain.csv
│   └── exoTest.csv
└── processed/
```

---
