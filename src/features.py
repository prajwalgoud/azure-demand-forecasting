import pandas as pd
import numpy as np

df = pd.read_csv("data/clean_usage_data.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])

df = df.sort_values(['region','timestamp'])

# Time features
df['hour'] = df['timestamp'].dt.hour
df['dayofweek'] = df['timestamp'].dt.dayofweek
df['month'] = df['timestamp'].dt.month

# Cyclical encoding (important for time series)
df['hour_sin'] = np.sin(2 * np.pi * df['hour']/24)
df['hour_cos'] = np.cos(2 * np.pi * df['hour']/24)

# Lag features
for lag in [1,3,6]:
    df[f'lag_{lag}'] = df.groupby('region')['usage_units'].shift(lag)

# Rolling features
df['rolling_mean_6'] = (
    df.groupby('region')['usage_units']
      .rolling(6)
      .mean()
      .reset_index(level=0, drop=True)
)

df['rolling_std_6'] = (
    df.groupby('region')['usage_units']
      .rolling(6)
      .std()
      .reset_index(level=0, drop=True)
)

df = df.dropna()

df.to_csv("data/feature_data.csv", index=False)

print("Advanced feature dataset:", df.shape)
