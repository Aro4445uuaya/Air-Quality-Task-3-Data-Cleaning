
import pandas as pd

df = pd.read_csv(
    "data/processed/transformed_data.csv"
)

df["Timestamp"] = pd.to_datetime(
    df["Timestamp"], errors="coerce"
)

columns = [
    "CO(GT)", "PT08.S1(CO)", "NMHC(GT)",
    "C6H6(GT)", "PT08.S2(NMHC)", "NOx(GT)",
    "PT08.S3(NOx)", "NO2(GT)", "PT08.S4(NO2)",
    "PT08.S5(O3)", "T", "RH", "AH"
]

results = []

for column in columns:
    values = df[column].dropna()

    q1 = values.quantile(0.25)
    q3 = values.quantile(0.75)
    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    flagged = df[
        (df[column] < lower) |
        (df[column] > upper)
    ][["Timestamp", column]].copy()

    for _, row in flagged.iterrows():
        results.append({
            "Timestamp": row["Timestamp"],
            "Sensor": column,
            "Value": row[column],
            "Lower_Bound": lower,
            "Upper_Bound": upper
        })

report = pd.DataFrame(results)

report.to_csv(
    "data/processed/outlier_investigation.csv",
    index=False
)

print("Potential outlier records:", len(report))
print("\nOutlier counts by sensor:")
print(report.groupby("Sensor").size())

print("\nSample flagged records:")
print(report.head(20))

print("\nSaved: data/processed/outlier_investigation.csv")
