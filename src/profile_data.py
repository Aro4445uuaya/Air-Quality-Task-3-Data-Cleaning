
import pandas as pd

file_path = "data/raw/AirQualityUCI.csv"

# Read original dataset
df = pd.read_csv(
    file_path,
    sep=";",
    decimal=","
)

# Remove completely empty rows and columns
df = df.dropna(how="all")
df = df.dropna(axis=1, how="all")

# Work on a separate copy
clean_df = df.copy()

# Replace -200 with NaN in numerical columns
numeric_columns = clean_df.select_dtypes(include="number").columns

clean_df[numeric_columns] = clean_df[numeric_columns].replace(-200, float("nan"))

print("\n--- MISSING VALUES AFTER REPLACEMENT ---")

missing_count = clean_df.isnull().sum()
missing_percentage = (missing_count / len(clean_df)) * 100

missing_report = pd.DataFrame({
    "Missing_Count": missing_count,
    "Missing_Percentage": missing_percentage.round(2)
})

print(missing_report)

print("\n--- UPDATED STATISTICAL SUMMARY ---")
print(clean_df.describe())

# Save cleaned intermediate dataset
output_path = "data/processed/air_quality_missing_values_handled.csv"

clean_df.to_csv(output_path, index=False)

print("\nProcessed dataset saved successfully!")
