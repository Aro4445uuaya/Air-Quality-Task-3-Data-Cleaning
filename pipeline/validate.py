
import pandas as pd
from pathlib import Path


def validate_data():

    input_file = Path("data/processed/transformed_data.csv")

    print("Starting data validation...")

    df = pd.read_csv(input_file)

    # Validate required columns
    required_columns = [
        "Date", "Time", "Timestamp",
        "CO(GT)", "NOx(GT)", "NO2(GT)", "T", "RH", "AH"
    ]

    missing_columns = [
        col for col in required_columns if col not in df.columns
    ]

    # Validate timestamps
    df["Timestamp"] = pd.to_datetime(
        df["Timestamp"], errors="coerce"
    )

    invalid_timestamps = df["Timestamp"].isna().sum()

    # Check duplicate rows and timestamps
    duplicate_rows = df.duplicated().sum()
    duplicate_timestamps = df["Timestamp"].duplicated().sum()

    # Check missing values
    missing_values = df.isna().sum().sum()

    # Check chronological order
    chronological = df["Timestamp"].is_monotonic_increasing

    # Check hourly gaps
    sorted_df = df.sort_values("Timestamp")
    time_difference = sorted_df["Timestamp"].diff()

    gaps = (
        time_difference > pd.Timedelta(hours=1)
    ).sum()

    print("\n--- DATA VALIDATION REPORT ---")
    print("Total records:", len(df))
    print("Missing required columns:", missing_columns)
    print("Invalid timestamps:", invalid_timestamps)
    print("Duplicate rows:", duplicate_rows)
    print("Duplicate timestamps:", duplicate_timestamps)
    print("Total missing values:", missing_values)
    print("Chronological order:", chronological)
    print("Intervals greater than 1 hour:", gaps)

    passed = (
        len(missing_columns) == 0
        and invalid_timestamps == 0
        and duplicate_rows == 0
        and duplicate_timestamps == 0
        and chronological
        and gaps == 0
    )

    print("\nValidation status:", "PASSED" if passed else "FAILED")

    if not passed:
        raise ValueError("Data validation failed. Check the report.")

    print("\nData validation completed successfully!")


if __name__ == "__main__":
    validate_data()
