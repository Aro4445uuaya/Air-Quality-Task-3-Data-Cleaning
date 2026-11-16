
import pandas as pd

file_path = "data/processed/air_quality_timestamp_checked.csv"

df = pd.read_csv(file_path)

df["Timestamp"] = pd.to_datetime(df["Timestamp"])

df = df.sort_values("Timestamp")

# Calculate difference between consecutive records
df["Time_Difference"] = df["Timestamp"].diff()

# Expected interval is one hour
gaps = df[df["Time_Difference"] > pd.Timedelta(hours=1)]

print("--- TIME GAP ANALYSIS ---")

print("Total records:", len(df))
print("Intervals greater than 1 hour:", len(gaps))

print("\nFirst 10 detected gaps:")
print(gaps[["Timestamp", "Time_Difference"]].head(10))

print("\nLargest time gap:")
print(df["Time_Difference"].max())

print("\nTime gap analysis completed!")
