
import pandas as pd

file_path = "data/raw/AirQualityUCI.csv"

df = pd.read_csv(
    file_path,
    sep=";",
    decimal=","
)

# Remove completely empty columns
df = df.dropna(axis=1, how="all")

print("\n--- DATASET OVERVIEW ---")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- FIRST 5 RECORDS ---")
print(df.head())

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())
