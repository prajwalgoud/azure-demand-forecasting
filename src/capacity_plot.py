import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/capacity_recommendations.csv")

plt.figure(figsize=(8,5))

plt.bar(df["region"], df["forecast_demand"], label="Forecast Demand")
plt.bar(df["region"], df["current_capacity"], alpha=0.5, label="Current Capacity")

plt.ylabel("Capacity Units")
plt.title("Demand vs Capacity")
plt.legend()

plt.show()