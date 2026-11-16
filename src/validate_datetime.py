
import pandas as pd

file_path = "data/processed/air_quality_missing_values_handled.csv"

df = pd.read_csv(file_path)

# Combine Date and Time
df["Timestamp"] = pd.to_datetime(
    df["Date"] + " " + df["Time"],
    format="%d/%m/%Y %H.%M.%S",
    errors="coerce"
)

print("--- TIMESTAMP VALIDATION ---")

print("Total records:", len(df))
print("Invalid timestamps:", df["Timestamp"].isna().sum())
print("Duplicate timestamps:", df["Timestamp"].duplicated().sum())

print("\nFirst 5 timestamps:")
print(df[["Date", "Time", "Timestamp"]].head())

print("\nEarliest timestamp:", df["Timestamp"].min())
print("Latest timestamp:", df["Timestamp"].max())

# Save validated intermediate data
df.to_csv(
    "data/processed/air_quality_timestamp_checked.csv",
    index=False
)

print("\nTimestamp validation completed!")
