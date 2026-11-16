
import pandas as pd

file_path = "data/processed/air_quality_timestamp_checked.csv"

df = pd.read_csv(file_path)

numeric_columns = df.select_dtypes(include="number").columns

report = pd.DataFrame({
    "Data_Type": df.dtypes.astype(str),
    "Missing_Count": df.isnull().sum(),
    "Missing_Percentage": (
        df.isnull().sum() / len(df) * 100
    ).round(2),
    "Unique_Values": df.nunique()
})

print("--- DATA QUALITY REPORT ---")
print(report)

print("\nTotal records:", len(df))
print("Duplicate rows:", df.duplicated().sum())
print("Duplicate timestamps:", df["Timestamp"].duplicated().sum())

report.to_csv(
    "data/processed/data_quality_report.csv"
)

print("\nData quality report saved successfully!")
