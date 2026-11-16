
import pandas as pd

file_path = "data/processed/transformed_data.csv"

df = pd.read_csv(file_path)

numeric_columns = df.select_dtypes(include="number").columns

print("\n--- NUMERICAL DATA ANALYSIS ---")

for column in numeric_columns:
    print(f"\nColumn: {column}")
    print("Minimum:", df[column].min())
    print("Maximum:", df[column].max())
    print("Mean:", round(df[column].mean(), 3))
    print("Median:", round(df[column].median(), 3))
    print("Standard Deviation:", round(df[column].std(), 3))

print("\n--- TIMESTAMP ANALYSIS ---")

df["Timestamp"] = pd.to_datetime(
    df["Timestamp"], errors="coerce"
)

print("Invalid timestamps:", df["Timestamp"].isna().sum())
print("Earliest:", df["Timestamp"].min())
print("Latest:", df["Timestamp"].max())

print("\n--- OUTLIER INVESTIGATION ---")

for column in numeric_columns:
    series = df[column].dropna()

    if len(series) == 0:
        continue

    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    outliers = ((series < lower) | (series > upper)).sum()

    print(column, "Potential outliers:", outliers)

