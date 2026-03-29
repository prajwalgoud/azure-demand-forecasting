# 🚀 Azure Demand Forecasting & Capacity Optimization

## 📌 Overview

An end-to-end system to **forecast cloud demand** and **optimize infrastructure capacity** using machine learning.
The project predicts future usage and recommends scaling actions (**Scale Up / Scale Down / Maintain**) to balance performance and cost.

---

## 🏗️ Workflow

```
Data → Cleaning → Feature Engineering → ML Model → Forecast → Capacity Decisions → API + Dashboard
```

---

## 📊 Dataset

* ~100–150 rows, 15 features
* Includes:

  * Usage metrics (usage_units, cost, availability)
  * External variables (market, economic, temperature)
  * Operational metrics (latency, request count)

---

## ✅ Milestones

### 🔹 Milestone 1 — Data Preparation

* Data cleaning, missing value handling
* Format standardization and validation

### 🔹 Milestone 2 — Modeling

* Feature engineering (lag, rolling, cyclical)
* Models: Random Forest, XGBoost
* Evaluation: MAE, RMSE

### 🔹 Milestone 3 — Optimization

* Capacity planning with buffer
* Peak & anomaly detection
* Cost optimization logic

### 🔹 Milestone 4 — Deployment

* FastAPI for prediction API
* Streamlit dashboard for user interaction

---

## ⚙️ How to Run

```bash
pip install -r requirements.txt
```

```bash
python src/preprocess.py
python src/features.py
python src/train_advanced.py
python src/capacity_engine.py
```

### Run API

```bash
uvicorn src.api:app --reload
```

### Run Dashboard

```bash
streamlit run src/app.py
```

---

## 🛠 Tech Stack

Python, Pandas, NumPy, Scikit-learn, XGBoost, FastAPI, Streamlit

---

## 👨‍💻 Author

Prajwal Goud
