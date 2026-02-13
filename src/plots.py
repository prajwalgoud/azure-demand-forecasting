import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/clean_usage_data.csv")

for r,g in df.groupby("region"):
    plt.plot(pd.to_datetime(g['timestamp']),
             g['usage_units'],
             label=r)

plt.legend()
plt.title("Usage by Region")
plt.show()
