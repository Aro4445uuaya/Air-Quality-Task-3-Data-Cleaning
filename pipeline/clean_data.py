
import pandas as pd
from pathlib import Path

input_file = Path("data/processed/transformed_data.csv")
output_file = Path("data/processed/cleaned_data.csv")

df = pd.read_csv(input_file)

sensor_columns = df.select_dtypes(
    include="number"
).columns.tolist()

# Flag records where every sensor reading is missing
df["quality_status"] = "AVAILABLE"

fully_missing = df[sensor_columns].isna().all(axis=1)

df.loc[fully_missing, "quality_status"] = "NO_SENSOR_READINGS"

# Save all records without deleting useful information
output_file.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_file, index=False)

print("--- CLEANING SUMMARY ---")
print("Original records:", len(df))
print("Available sensor records:", (~fully_missing).sum())
print("Fully missing sensor records:", fully_missing.sum())
print("Final records:", len(df))
print("Records deleted:", 0)
print("Output:", output_file)
