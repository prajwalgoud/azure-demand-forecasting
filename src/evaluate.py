import pandas as pd
import joblib
import matplotlib.pyplot as plt

df = pd.read_csv("data/feature_data.csv")

FEATURES = [
    'hour','dayofweek','month',
    'lag_1','lag_3','rolling_mean_3',
    'market_index','economic_index',
    'cloud_price_index','network_latency_ms',
    'request_count','scaling_events',
    'temperature_c'
]

model = joblib.load("model.pkl")

split = int(len(df) * 0.8)

test_df = df.iloc[split:].copy()

preds = model.predict(test_df[FEATURES])

plt.plot(test_df['usage_units'].values, label="Actual")
plt.plot(preds, label="Predicted")

plt.legend()
plt.title("Actual vs Predicted Demand")
plt.show()