
import pandas as pd

df = pd.read_csv(
    "data/processed/transformed_data.csv"
)

numeric = df.select_dtypes(include="number")

report = pd.DataFrame({
    "Valid_Count": numeric.count(),
    "Missing_Count": numeric.isna().sum(),
    "Missing_Percentage": (
        numeric.isna().mean() * 100
    ).round(2)
})

print("\n--- MISSING VALUE ANALYSIS ---")
print(report.to_string())

print("\n--- COMPLETE RECORD ANALYSIS ---")

print(
    "Rows with all sensor readings:",
    numeric.dropna().shape[0]
)

print(
    "Rows with at least one missing reading:",
    numeric.isna().any(axis=1).sum()
)

print(
    "Rows missing every sensor reading:",
    numeric.isna().all(axis=1).sum()
)

report.to_csv(
    "data/processed/missing_value_analysis.csv"
)

print("\nReport saved successfully!")
