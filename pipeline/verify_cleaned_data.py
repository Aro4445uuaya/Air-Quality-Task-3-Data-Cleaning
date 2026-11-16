
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

print("--- CLEANING VERIFICATION ---")

print("Original rows:", len(original))
print("Cleaned rows:", len(cleaned))

print(
    "Original missing values:",
    original[sensor_columns].isna().sum().sum()
)

print(
    "Cleaned missing values:",
    cleaned[sensor_columns].isna().sum().sum()
)

print(
    "Available records:",
    (cleaned["quality_status"] == "AVAILABLE").sum()
)

print(
    "Fully missing records:",
    (cleaned["quality_status"] == "NO_SENSOR_READINGS").sum()
)

print(
    "Status column exists:",
    "quality_status" in cleaned.columns
)

print("\nVerification completed!")
