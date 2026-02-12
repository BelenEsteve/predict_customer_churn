# Predict Customer Churn

> ML DevOps Engineer Nanodegree Project – Udacity
>
> Production-ready churn prediction pipeline with logging, testing, and model interpretability.

## Table of contents
- [Overview](#overview)
- [Project Motivation](#project-motivation)
- [Features](#features)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Logging](#logging)
- [Data Analysis](#data-analysis)
- [Model Artifacts](#model-artifacts)
- [Technologies Used](#technologies-used)
- [ML Engineering Highlights](#ml-engineering-highlights)
- [License](#license)
- [Contact Information](#contact-information)
- [Aknowledgments](#acknowledgments)

## Overview
This project builds an end-to-end machine learning pipeline to predict customer churn using historical banking data.

The pipeline:
- Performs exploratory data analysis (EDA)
- Conducts feature engineering
- Trains classification models
- Evaluates model performance
- Generates model interpretability outputs
- Logs execution steps
- Includes unit testing for production readiness

The goal is to identify customers at risk of churn and support data-driven retention strategies.

## Project Motivation

Customer churn is a critical business problem. Acquiring new customers is often more expensive than retaining existing ones.

This project demonstrates:
- Building a production-style ML pipeline
- Applying ML DevOps best practices
- Writing testable and maintainable code
- Logging and monitoring ML workflows
- Ensuring reproducibility

This repository is designed to reflect industry-level ML engineering standards.

## Features

✔ Modular ML pipeline

✔ Feature encoding with target-based encoding

✔ Logistic Regression & Random Forest models

✔ GridSearch hyperparameter tuning

✔ ROC curve evaluation

✔ SHAP interpretability

✔ Feature importance visualization

✔ Automated unit testing

✔ Structured logging

✔ Artifact persistence (models & plots)


## Project Structure
```
predict_customer_churn/
│
├── data/
│   └── bank_data.csv
│
├── images/
│   ├── eda/
│   │   ├── churn_labels.png
│   │   ├── customer_age.png
│   │   ├── heatmap.png
│   │   ├── marital_status.png
│   │   └── total_trans_ct.png
│   │
│   └── results/
│       ├── logistic_regression_random_forest_best_roc_curve.png
│       ├── logistic_regression_random_forest_roc_curve.png
│       ├── random_forest_classification_report.png
│       ├── random_forest_feature_importance.png
│       └── random_forest_shap_summary_plot.png
│
├── logs/
│
├── models/
│
├── churn_library.py
├── churn_script_logging_and_tests.py
├── constants.py
├── requirements.in
├── requirements.txt
└── LICENSE
```

## Dataset

The dataset contains:
- Customer demographics
- Account information
- Transaction behavior
- Attrition labels

Location:
```
data/bank_data.csv
```
The target variable is derived from:
```
Attrition_Flag
```

## Installation
Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
#venv\Scripts\activate     # Windows
```
Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

#### Run Main Pipeline
This performs:
- Data loading
- EDA
- Feature engineering
- Model training
- Evaluation
- Saving outputs
- Logging

```bash
python predict_customer_churn/churn_library.py
```
The logging generated is in `logs/churn_logs.log`.

#### Unit Tests
Unit tests cover all major functions in `churn_library.py`.

Run:

```bash
pytest -s predict_customer_churn/churn_script_logging_and_tests.py > predict_customer_churn/logs/test_logs.log
```

This generates `logs/test_logs.log`.

All functions are validated for:
- Data integrity
- Feature engineering correctness
- Model training
- Model saving
- Artifact generation


## Logging
Logs are stored in `predict_customer/logs`:

| File             | Description                  |
| ---------------- | ---------------------------- |
| `churn_logs.log` | Main pipeline execution logs |
| `test_logs.log`  | Pytest execution logs        |

Logging ensures traceability and debugging capability.

## Data Analysis

Saved analysis include:
- Distribution of labels
- Distribution of some attributes
- Heatmap of correlation between attributes

Stored in:
```
images/eda/
```

## Model Artifacts

Saved artifacts include:
- Trained Logistic Regression model
- Trained Random Forest model
- ROC curves
- SHAP summary plot
- Feature importance plots
- Classification reports

Stored in:
```
models/
images/results/
```

## Technologies Used

- Python 3.10+
- pandas
- NumPy
- scikit-learn
- matplotlib
- seaborn
- SHAP
- pytest
- joblib

## ML Engineering Highlights

This project demonstrates:
- Reproducible ML pipelines
- Separation of concerns
- Logging best practices
- Robust testing
- Model interpretability
- Artifact management

## License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

See the LICENSE file for details.

## Contact Information

If you would like to discuss this project or explore collaboration opportunities:

**Belen Esteve Cogollos**
Computer Vision & MLOps Engineer

- GitHub: https://github.com/BelenEsteve
- LinkedIn: https://www.linkedin.com/in/belenestevecogollos
- Email: belen.esteve.co@gmail.com

## Acknowledgments

This repository was developed as part of the Udacity Machine Learning DevOps Engineer Nanodegree.

It leverages several open-source libraries maintained by the global developer community. Their work makes modern machine learning development possible.