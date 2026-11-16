
import sys
import subprocess
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import URL, create_engine, text
import os

BASE_DIR = Path(__file__).resolve().parents[1]
PIPELINE_DIR = BASE_DIR / "pipeline"

load_dotenv(BASE_DIR / ".env")


def run_stage(script_name):
    script_path = PIPELINE_DIR / script_name

    print(f"\n{'=' * 45}")
    print(f"RUNNING: {script_name}")
    print("=" * 45)

    subprocess.run(
        [sys.executable, str(script_path)],
        cwd=BASE_DIR,
        check=True
    )


def verify_database(expected_records):
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
        with engine.connect() as connection:
            actual_records = connection.execute(
                text("SELECT COUNT(*) FROM air_quality_readings")
            ).scalar()

        print("\n--- FINAL PIPELINE VERIFICATION ---")
        print("Expected records:", expected_records)
        print("Database records:", actual_records)

        if actual_records != expected_records:
            raise ValueError("Database record count mismatch!")

        print("Pipeline verification: PASSED")

    finally:
        engine.dispose()


def main():
    print("AIR QUALITY DATA ENGINEERING PIPELINE")

    run_stage("extract.py")
    run_stage("transform.py")
    run_stage("validate.py")

    transformed_file = (
        BASE_DIR / "data" / "processed" / "transformed_data.csv"
    )
    expected_records = len(pd.read_csv(transformed_file))

    # Check whether data has already been loaded
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
        with engine.connect() as connection:
            existing_records = connection.execute(
                text("SELECT COUNT(*) FROM air_quality_readings")
            ).scalar()
    finally:
        engine.dispose()

    if existing_records == 0:
        run_stage("load.py")
    elif existing_records == expected_records:
        print("\nLoad skipped: matching records already exist.")
    else:
        raise ValueError(
            "Existing database count differs from source. "
            "Review before loading."
        )

    verify_database(expected_records)

    print("\nALL PIPELINE STAGES COMPLETED!")


if __name__ == "__main__":
    main()
