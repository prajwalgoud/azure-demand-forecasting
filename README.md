# Azure Demand Forecasting & Capacity Optimization System

## Project Overview

This project builds a predictive and decision-support system for forecasting Azure cloud resource demand and optimizing infrastructure capacity. The system uses historical usage data, external drivers, and machine learning models to forecast demand and recommend scaling decisions that minimize cost while maintaining service reliability.

The project is implemented in Python and follows a milestone-based development approach:

* **Milestone 1:** Data Collection & Preparation
* **Milestone 2:** Demand Forecast Modeling
* **Milestone 3:** Capacity Optimization & Decision Engine

The final system simulates how cloud providers manage infrastructure planning, demand spikes, and cost optimization.

---

# System Architecture

```
Data Collection
      ↓
Data Cleaning & Validation
      ↓
Feature Engineering
      ↓
Machine Learning Forecast Model
      ↓
Capacity Optimization Engine
      ↓
Infrastructure Scaling Decisions
      ↓
Cost Optimization Report
```

---

# Dataset

A realistic synthetic dataset is used because real Azure infrastructure telemetry is not publicly available.

Dataset characteristics:

* **Rows:** ~100–150
* **Columns:** 15
* **Time Resolution:** Hourly
* **Regions:** US East, India South, Europe West
* **Services:** Compute and Storage

### Core Metrics

* timestamp
* region
* service_type
* usage_units
* cost_usd
* availability_pct

### Calendar Features

* is_holiday
* is_weekend

### External Variables

* market_index
* economic_index
* cloud_price_index
* temperature_c

### Operational Indicators

* network_latency_ms
* request_count
* scaling_events

These variables help simulate real-world cloud demand drivers.

---

# Milestone 1 — Data Collection & Preparation

## Objective

Prepare a clean and consistent dataset suitable for forecasting models.

### Tasks Completed

* Collected and generated cloud demand dataset
* Added external economic and market variables
* Standardized timestamp and categorical formats
* Normalized region names
* Handled missing values using interpolation
* Forward-filled availability metrics
* Removed duplicates
* Validated data ranges and consistency

### Output Files

```
data/
   azure_realistic_100x15.csv
   clean_usage_data.csv
```

### Scripts

```
src/preprocess.py
src/validate.py
src/plots.py
```

---

# Milestone 2 — Demand Forecast Modeling

## Objective

Develop machine learning models to forecast cloud demand using historical data and external drivers.

### Feature Engineering

Generated predictive features:

* Time-based features
* Cyclical encoding (hour_sin, hour_cos)
* Lag features
* Rolling statistics

Examples:

```
lag_1
lag_3
lag_6
rolling_mean_6
rolling_std_6
```

### Machine Learning Models

Two models were trained:

* Random Forest Regressor
* XGBoost Regressor

### Model Evaluation Metrics

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

### Advanced Modeling Techniques

* TimeSeriesSplit cross-validation
* Hyperparameter tuning (GridSearchCV)
* Residual analysis
* Feature importance analysis

### Output

```
model/best_model.pkl
data/feature_data.csv
```

---

# Milestone 3 — Capacity Optimization & Decision Engine

## Objective

Convert demand predictions into infrastructure scaling decisions.

Instead of only predicting demand, the system now recommends operational actions.

### Key Components

### 1. Capacity Buffer Logic

A safety buffer ensures infrastructure reliability.

```
required_capacity = forecast * 1.15
```

### 2. Scaling Decision Rules

| Condition                            | Action           |
| ------------------------------------ | ---------------- |
| Required capacity > current capacity | Scale Up         |
| Demand < 40% capacity                | Scale Down       |
| Peak detected                        | Aggressive Scale |
| Normal usage                         | Maintain         |

### 3. Peak Demand Detection

Detects sudden spikes in workload using rolling statistics.

```
peak_threshold = rolling_mean + 2 * rolling_std
```

### 4. Anomaly Detection

Identifies abnormal demand using Z-score.

```
anomaly = |zscore| > 3
```

### 5. Cost Optimization

Calculates wasted infrastructure cost due to over-provisioning.

Example:

| Region  | Forecast | Capacity | Action     | Wasted Cost |
| ------- | -------- | -------- | ---------- | ----------- |
| US East | 210      | 260      | Scale Down | $22/hr      |

### Output

```
data/capacity_recommendations.csv
```

### Example Result

| Region      | Forecast | Capacity | Action     |
| ----------- | -------- | -------- | ---------- |
| US East     | 212      | 200      | Scale Up   |
| India South | 92       | 180      | Scale Down |
| Europe West | 158      | 160      | Maintain   |

---

# Explainability

SHAP explainability is used to understand feature contributions to demand predictions.

Key insights include:

* Lag demand features strongly influence predictions
* Market index impacts cloud usage trends
* Request count correlates with demand spikes

---

# Project Structure

```
azure-demand-forecasting/
│
├── data/
│   ├── azure_realistic_100x15.csv
│   ├── clean_usage_data.csv
│   ├── feature_data.csv
│   └── capacity_recommendations.csv
│
├── src/
│   ├── preprocess.py
│   ├── features.py
│   ├── train_advanced.py
│   ├── evaluate.py
│   ├── feature_importance.py
│   ├── capacity_engine.py
│   ├── capacity_plot.py
│   └── explain_model.py
│
├── model/
│   └── best_model.pkl
│
├── requirements.txt
└── README.md
```

---

# Installation

Create environment and install dependencies:

```
pip install -r requirements.txt
```

---

# Running the Project

### Data Preparation

```
python src/preprocess.py
```

### Feature Engineering

```
python src/features.py
```

### Train Model

```
python src/train_advanced.py
```

### Evaluate Model

```
python src/evaluate.py
```

### Capacity Optimization

```
python src/capacity_engine.py
```

---

# Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Matplotlib
* SHAP

---

# Future Work (Milestone 4)

* Streamlit interactive dashboard
* FastAPI prediction service
* Automated forecasting pipeline
* Infrastructure monitoring simulation

---

# Author

Prajwal Goud
B.Tech Computer Science
Azure Demand Forecasting Project

