
import pandas as pd

df = pd.read_csv(
    "data/processed/transformed_data.csv"
)

sensor_columns = df.select_dtypes(
    include="number"
).columns

# Find records where all sensor readings are missing
fully_missing = df[
    df[sensor_columns].isna().all(axis=1)
].copy()

print("Fully missing sensor records:", len(fully_missing))

print("\n--- RECORD DETAILS ---")
print(
    fully_missing[
        ["Date", "Time", "Timestamp"]
    ].to_string(index=False)
)

# Check missing-value distribution per record
missing_distribution = (
    df[sensor_columns]
    .isna()
    .sum(axis=1)
    .value_counts()
    .sort_index()
)

print("\n--- MISSING VALUES PER RECORD ---")
print(missing_distribution.to_string())

fully_missing.to_csv(
    "data/processed/fully_missing_records.csv",
    index=False
)

print("\nInvestigation report saved!")
