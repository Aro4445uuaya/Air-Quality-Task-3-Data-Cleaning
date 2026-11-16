
import pandas as pd
from pathlib import Path


def extract_data():

    # Define source and destination
    source_file = Path("data/raw/AirQualityUCI.csv")
    output_file = Path("data/processed/extracted_data.csv")

    print("Starting data extraction...")

    # Check whether source file exists
    if not source_file.exists():
        raise FileNotFoundError(
            f"Dataset not found: {source_file}"
        )

    # Read original CSV file
    df = pd.read_csv(
        source_file,
        sep=";",
        decimal=","
    )

    original_rows = len(df)

    # Remove completely empty rows and columns
    df = df.dropna(how="all")
    df = df.dropna(axis=1, how="all")

    # Create output directory if necessary
    output_file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save extracted data without changing sensor values
    df.to_csv(output_file, index=False)

    print("\n--- EXTRACTION SUMMARY ---")
    print("Source file:", source_file)
    print("Original rows:", original_rows)
    print("Extracted rows:", len(df))
    print("Extracted columns:", len(df.columns))
    print("Removed empty rows:", original_rows - len(df))
    print("Output file:", output_file)

    print("\nData extraction completed successfully!")

    return df


if __name__ == "__main__":
    extract_data()
