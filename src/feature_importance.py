import joblib
import pandas as pd
import matplotlib.pyplot as plt

# Load feature dataset
df = pd.read_csv("data/feature_data.csv")

# Use EXACT same feature list from train_advanced.py
FEATURES = [
    'hour_sin','hour_cos','dayofweek','month',
    'lag_1','lag_3','lag_6',
    'rolling_mean_6','rolling_std_6',
    'market_index','economic_index',
    'cloud_price_index','network_latency_ms',
    'request_count','scaling_events','temperature_c'
]

# Load best model
model = joblib.load("best_model.pkl")

importances = model.feature_importances_

print("Number of features used in model:", len(importances))
print("Number of feature names:", len(FEATURES))

plt.figure(figsize=(10,6))
plt.barh(FEATURES, importances)
plt.title("Feature Importance")
plt.xlabel("Importance Score")
plt.tight_layout()
plt.show()