import pandas as pd

df = pd.read_csv("data/azure_milestone1.csv")

print("Raw shape:", df.shape)

# format fixes
df['timestamp'] = pd.to_datetime(df['timestamp'])

df['region'] = (
    df['region']
    .str.lower()
    .str.strip()
    .str.replace(" ", "-")
)

df['service_type'] = df['service_type'].str.lower()

df = df.sort_values(['region','timestamp'])

# ---- FIXED GROUP INTERPOLATION ----
df['usage_units'] = (
    df.groupby('region')['usage_units']
      .apply(lambda s: s.interpolate())
      .reset_index(level=0, drop=True)
)

df['cost_usd'] = df['cost_usd'].fillna(df['usage_units'] * 0.5)

df['availability_pct'] = (
    df.groupby('region')['availability_pct']
      .apply(lambda s: s.ffill())
      .reset_index(level=0, drop=True)
)

# validation filters
df = df[df['availability_pct'].between(0,100)]
df = df[df['usage_units'] > 0]

df = df.drop_duplicates(['timestamp','region','service_type'])

print("\nNull report:\n", df.isnull().sum())

df.to_csv("data/clean_usage_data.csv", index=False)

print("\nSaved clean_usage_data.csv")
