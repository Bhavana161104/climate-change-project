import pandas as pd

df = pd.read_csv("GlobalLandTemperaturesByCity.csv")
df_small = df.sample(5000, random_state=42)
df_small.to_csv("small_data.csv", index=False)

print("Small dataset created!")