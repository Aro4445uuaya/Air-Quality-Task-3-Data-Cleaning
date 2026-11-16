
import pandas as pd

df = pd.read_csv(
    "data/processed/transformed_data.csv"
)

# Broad physical plausibility checks.
# These are investigation thresholds, not official UCI limits.
checks = {
    "CO(GT)": (0, None),
    "PT08.S1(CO)": (0, None),
    "NMHC(GT)": (0, None),
    "C6H6(GT)": (0, None),
    "PT08.S2(NMHC)": (0, None),
    "NOx(GT)": (0, None),
    "PT08.S3(NOx)": (0, None),
    "NO2(GT)": (0, None),
    "PT08.S4(NO2)": (0, None),
    "PT08.S5(O3)": (0, None),
    "T": (-10, 60),
    "RH": (0, 100),
    "AH": (0, None)
}

print("\n--- SENSOR RANGE INVESTIGATION ---")

for column, (lower, upper) in checks.items():
    values = df[column].dropna()

    invalid = pd.Series(False, index=values.index)

    if lower is not None:
        invalid |= values < lower

    if upper is not None:
        invalid |= values > upper

    print(
        column,
        "| Records checked:", len(values),
        "| Outside investigation range:", invalid.sum()
    )

print("\nRange investigation completed.")
