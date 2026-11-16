
import pandas as pd

original = pd.read_csv(
    "data/processed/transformed_data.csv"
)

cleaned = pd.read_csv(
    "data/processed/cleaned_data.csv"
)

sensor_columns = original.select_dtypes(
    include="number"
).columns

print("--- SENSOR DATA INTEGRITY CHECK ---")

for column in sensor_columns:
    same = original[column].equals(cleaned[column])
    print(column, ":", "UNCHANGED" if same else "CHANGED")

all_same = all(
    original[col].equals(cleaned[col])
    for col in sensor_columns
)

print("\nAll sensor values unchanged:", all_same)
print("Original rows:", len(original))
print("Cleaned rows:", len(cleaned))
