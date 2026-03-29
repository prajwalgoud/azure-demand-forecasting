from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Load model
model = joblib.load("best_model.pkl")

FEATURES = [
    'hour_sin','hour_cos','dayofweek','month',
    'lag_1','lag_3','lag_6',
    'rolling_mean_6','rolling_std_6',
    'market_index','economic_index',
    'cloud_price_index','network_latency_ms',
    'request_count','scaling_events','temperature_c'
]

# Sample capacity config
capacity = {
    "us-east": 200,
    "india-south": 180,
    "europe-west": 160
}

BUFFER = 1.15

@app.get("/")
def home():
    return {"message": "Azure Demand Forecast API Running"}

@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame([data])

    prediction = model.predict(df[FEATURES])[0]

    region = data.get("region", "us-east")
    current_capacity = capacity.get(region,150)

    required_capacity = prediction * BUFFER

    if required_capacity > current_capacity:
        action = "Scale Up"
    elif prediction < current_capacity * 0.4:
        action = "Scale Down"
    else:
        action = "Maintain"

    return {
        "predicted_demand": round(prediction,2),
        "required_capacity": round(required_capacity,2),
        "action": action
    }