import streamlit as st
import requests

st.title("Azure Demand Forecast Dashboard")

st.sidebar.header("Input Features")

region = st.sidebar.selectbox(
    "Region", ["us-east","india-south","europe-west"]
)

hour = st.sidebar.slider("Hour", 0, 23)
dayofweek = st.sidebar.slider("Day of Week", 0, 6)

market_index = st.sidebar.slider("Market Index", 90, 110, 100)
economic_index = st.sidebar.slider("Economic Index", 90, 110, 95)

request_count = st.sidebar.slider("Request Count", 50, 500, 200)

# dummy values for required features
data = {
    "region": region,
    "hour_sin": 0.5,
    "hour_cos": 0.5,
    "dayofweek": dayofweek,
    "month": 2,
    "lag_1": 150,
    "lag_3": 140,
    "lag_6": 130,
    "rolling_mean_6": 145,
    "rolling_std_6": 10,
    "market_index": market_index,
    "economic_index": economic_index,
    "cloud_price_index": 1.0,
    "network_latency_ms": 20,
    "request_count": request_count,
    "scaling_events": 1,
    "temperature_c": 27
}

if st.button("Predict Demand"):

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=data
    )

    result = response.json()

    st.subheader("Prediction Results")

    st.write("Predicted Demand:", result["predicted_demand"])
    st.write("Required Capacity:", result["required_capacity"])
    st.write("Action:", result["action"])