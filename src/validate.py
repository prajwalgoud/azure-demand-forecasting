import pandas as pd

df = pd.read_csv("data/clean_usage_data.csv")

print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())

print("\nNulls:\n", df.isnull().sum())

print("\nDuplicate rows:",
      df.duplicated(['timestamp','region','service_type']).sum())

print("\nUsage range:",
      df['usage_units'].min(),
      df['usage_units'].max())
