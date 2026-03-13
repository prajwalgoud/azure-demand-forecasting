import pandas as pd
import joblib
import numpy as np

# Load feature dataset
df = pd.read_csv("data/feature_data.csv")

# Load trained model
model = joblib.load("best_model.pkl")

# Same feature list used in training
FEATURES = [
    'hour_sin','hour_cos','dayofweek','month',
    'lag_1','lag_3','lag_6',
    'rolling_mean_6','rolling_std_6',
    'market_index','economic_index',
    'cloud_price_index','network_latency_ms',
    'request_count','scaling_events','temperature_c'
]

# Predict demand
df["predicted_demand"] = model.predict(df[FEATURES])

# Current infrastructure capacity (simulated)
capacity = {
    "us-east": 200,
    "india-south": 180,
    "europe-west": 160
}

BUFFER = 1.15
COST_PER_UNIT = 0.45

results = []

for region, group in df.groupby("region"):

    latest = group.iloc[-1]

    forecast = latest["predicted_demand"]

    current_capacity = capacity.get(region,150)

    required_capacity = forecast * BUFFER

    # Decision logic
    if required_capacity > current_capacity:
        action = "Scale Up"

    elif forecast < current_capacity * 0.40:
        action = "Scale Down"

    else:
        action = "Maintain"

    # Cost estimation
    provision_cost = current_capacity * COST_PER_UNIT
    optimal_cost = required_capacity * COST_PER_UNIT

    results.append({
        "region": region,
        "forecast_demand": round(forecast,2),
        "current_capacity": current_capacity,
        "required_capacity": round(required_capacity,2),
        "action": action,
        "current_cost_per_hr": round(provision_cost,2),
        "optimal_cost_per_hr": round(optimal_cost,2)
    })

result_df = pd.DataFrame(results)

print("\nCapacity Optimization Decisions\n")
print(result_df)

result_df.to_csv("data/capacity_recommendations.csv",index=False)

print("\nSaved results → data/capacity_recommendations.csv")