
import os
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine, URL, text

# Project paths
BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = BASE_DIR / "data" / "processed" / "transformed_data.csv"

# Load environment variables
load_dotenv(BASE_DIR / ".env")

def load_data():

    print("Starting data loading...")

    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

    # Read transformed data
    df = pd.read_csv(INPUT_FILE)

    # Convert timestamp column
    df["Timestamp"] = pd.to_datetime(
        df["Timestamp"], errors="coerce"
    )

    if df["Timestamp"].isna().any():
        raise ValueError("Invalid timestamps found. Loading stopped.")

    # Database configuration
    db_url = URL.create(
        drivername="mysql+pymysql",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", "3306")),
        database=os.getenv("DB_NAME")
    )

    engine = create_engine(db_url)

    try:
        # Check existing records before loading
        with engine.connect() as connection:
            existing_count = connection.execute(
                text("SELECT COUNT(*) FROM air_quality_readings")
            ).scalar()

        if existing_count > 0:
            raise RuntimeError(
                f"Table already contains {existing_count} records. "
                "Load stopped to prevent duplicate data."
            )

        # Load records into MySQL
        df.to_sql(
            name="air_quality_readings",
            con=engine,
            if_exists="append",
            index=False,
            chunksize=500
        )

        # Verify loaded records
        with engine.connect() as connection:
            loaded_count = connection.execute(
                text("SELECT COUNT(*) FROM air_quality_readings")
            ).scalar()

        print("\n--- DATA LOADING SUMMARY ---")
        print("Source records:", len(df))
        print("Records in MySQL:", loaded_count)
        print("Database:", os.getenv("DB_NAME"))
        print("Table: air_quality_readings")

        if loaded_count != len(df):
            raise ValueError("Row count mismatch after loading!")

        print("\nData loading completed successfully!")

    finally:
        engine.dispose()


if __name__ == "__main__":
    load_data()
