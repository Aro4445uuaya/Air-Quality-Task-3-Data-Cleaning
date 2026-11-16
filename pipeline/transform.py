
import pandas as pd
from pathlib import Path


def transform_data():

    input_file = Path("data/processed/extracted_data.csv")
    output_file = Path("data/processed/transformed_data.csv")

    print("Starting data transformation...")

    # Read extracted data
    df = pd.read_csv(input_file)

    original_rows = len(df)

    # Replace -200 with NaN in numerical columns
    numeric_columns = df.select_dtypes(include="number").columns

    missing_before = (df[numeric_columns] == -200).sum().sum()

    df[numeric_columns] = df[numeric_columns].replace(
        -200, float("nan")
    )

    # Combine Date and Time into a Timestamp
    df["Timestamp"] = pd.to_datetime(
        df["Date"] + " " + df["Time"],
        format="%d/%m/%Y %H.%M.%S",
        errors="coerce"
    )

    # Check invalid timestamps
    invalid_timestamps = df["Timestamp"].isna().sum()

    # Create output directory
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Save transformed dataset
    df.to_csv(output_file, index=False)

    print("\n--- TRANSFORMATION SUMMARY ---")
    print("Input records:", original_rows)
    print("Output records:", len(df))
    print("Numeric columns:", len(numeric_columns))
    print("-200 values converted to NaN:", missing_before)
    print("Invalid timestamps:", invalid_timestamps)
    print("Output file:", output_file)

    print("\nData transformation completed!")


if __name__ == "__main__":
    transform_data()
