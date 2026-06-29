# Exoplanet Detection AI

An end-to-end Machine Learning project for detecting exoplanets from astronomical light curve data.

## Project Overview

When a planet passes in front of its host star, the observed brightness of the star decreases slightly. This phenomenon is called a **transit event**.

The objective of this project is to build an AI-powered pipeline capable of identifying exoplanet transit signals from light curve data.

This project focuses on:

* Astronomy fundamentals
* Time-series analysis
* Data preprocessing
* Machine Learning
* Model evaluation
* Software engineering best practices
* Research-oriented development

---

## Team

### Aniruddha More

* Python
* AI/ML
* Data Science
* Backend Development
* Project Implementation

### Devi Chatterjee

* Astronomy Research
* Space Science
* Domain Understanding
* Literature Review

---

## Current Scope (MVP)

Binary Classification

Classes:

* Exoplanet Present
* No Exoplanet Present

We are intentionally ignoring:

* Eclipsing binaries
* Stellar variability classification
* Multi-class classification
* Transit parameter estimation

These features may be added in future versions.

---

## Dataset

This project uses a curated exoplanet dataset derived from Kepler observations.

The dataset is NOT stored in GitHub because it exceeds GitHub's file size limits.

### Download Dataset

Dataset Link:

https://drive.google.com/file/d/1wpda_oZ_Leo7GqxBK3JlRotYmSs8MWW8/view?usp=sharing

---

## Dataset Setup

Create the following structure:

```text
data/
└── raw/
    ├── exoTrain.csv
    └── exoTest.csv
```

Place the downloaded files inside:

```text
data/raw/
```

Expected files:

```text
data/raw/exoTrain.csv
data/raw/exoTest.csv
```

---

## Project Structure

```text
exoplanet-detection-ai/

├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_positive_sample_analysis.ipynb
│   ├── 02_dataset_exploration.ipynb
│   └── 03_preprocessing_experiments.ipynb
│
├── src/
│   ├── data/
│   │   ├── loader.py
│   │   └── validation.py
│   │
│   ├── visualization/
│   │   └── lightcurve_plots.py
│   │
│   ├── preprocessing/
│   │
│   ├── features/
│   │
│   ├── models/
│   │
│   └── utils/
│
├── reports/
│   └── figures/
│
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Environment Setup

### Clone Repository

```bash
git clone https://github.com/Aniruddha072/exoplanet-detection-ai.git

cd exoplanet-detection-ai
```

---

### Create Virtual Environment

Windows:

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Verify Installation

```bash
python -c "import pandas, numpy, matplotlib"
```

No errors should appear.

---

## Running The Notebook

Launch Jupyter:

```bash
jupyter notebook
```

or open the notebook directly in VS Code.

Current notebook:

```text
notebooks/01_positive_sample_analysis.ipynb
```

---

## Current Progress

### Completed

* Dataset collection
* Repository setup
* Initial light curve visualization
* Project restructuring
* Environment setup

### In Progress

* Positive sample analysis
* Dataset exploration

### Next Steps

1. Positive sample analysis
2. Dataset exploration
3. Data preprocessing
4. Feature engineering
5. Baseline ML models
6. Advanced ML models
7. Evaluation
8. Deployment

---

## Future Roadmap

### Version 1

Binary Classification

* Planet
* No Planet

### Version 2

Multi-Class Classification

* Exoplanet
* Eclipsing Binary
* Stellar Variability
* Noise

### Version 3

Transit Parameter Estimation

* Transit Depth
* Transit Duration
* Orbital Period

### Version 4

Deployment

* FastAPI
* Streamlit
* Docker

---

## License

MIT License
