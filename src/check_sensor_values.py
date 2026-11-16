
import pandas as pd

file_path = "data/processed/air_quality_timestamp_checked.csv"

df = pd.read_csv(file_path)

numeric_columns = df.select_dtypes(include="number").columns

print("--- SENSOR VALUE VALIDATION ---")

for column in numeric_columns:
    print(f"\n{column}")
    print("Minimum:", df[column].min())
    print("Maximum:", df[column].max())
    print("Missing:", df[column].isna().sum())

print("\nSensor value inspection completed!")
