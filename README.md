# Air Quality Sensor Data Engineering – Task 3
## Data Cleaning and Validation

### Project Overview
This project focuses on analysing, cleaning, and validating the output of the Week 2 Air Quality Sensor Data Engineering ETL pipeline.

The project uses the UCI Air Quality Dataset to investigate missing values, potential outliers, sensor ranges, and data integrity.

### Objectives
- Analyse missing sensor readings.
- Identify potential statistical outliers using the IQR method.
- Perform preliminary sensor range checks.
- Investigate records with all sensor readings missing.
- Create a cleaned dataset with quality-status indicators.
- Verify that original sensor measurements remain unchanged.

### Technologies Used
- Python
- Pandas
- NumPy
- MySQL
- Visual Studio Code
- Git and GitHub

### Data Cleaning and Analysis
The Week 2 transformed dataset contained 9,357 records and 13 numeric sensor columns.

Key findings:
- 16,701 missing sensor values.
- 1,659 potential IQR outlier flags across sensor columns.
- 31 records with all 13 sensor readings missing.
- Zero values outside the selected preliminary screening ranges.
- Zero duplicate rows.

### Cleaning Approach
A separate cleaned dataset was created with an additional `quality_status` column.

| Status | Description |
|---|---|
| AVAILABLE | At least one sensor reading is available |
| NO_SENSOR_READINGS | All 13 sensor readings are missing |

All 9,357 records were retained. No sensor values were deleted or imputed.

### Verification Results
- Original records: 9,357
- Cleaned records: 9,357
- Original missing values: 16,701
- Cleaned missing values: 16,701
- Sensor columns verified: 13
- Sensor values changed: 0
- Data integrity check: PASSED

### Project Structure
```text
Air-Quality-Task-3-Data-Cleaning/
│
├── pipeline/
│   ├── data_quality_analysis.py
│   ├── outlier_investigation.py
│   ├── sensor_range_check.py
│   ├── missing_value_analysis.py
│   ├── fully_missing_investigation.py
│   ├── clean_data.py
│   ├── verify_cleaned_data.py
│   └── data_integrity_check.py
│
├── data/
│   └── processed/
│       ├── cleaned_data.csv
│       ├── missing_value_analysis.csv
│       ├── outlier_investigation.csv
│       └── fully_missing_records.csv
│
├── requirements.txt
└── README.md
```

### Dataset Reference
UCI Machine Learning Repository – Air Quality Dataset

https://archive.ics.uci.edu/dataset/360/air+quality

### Documentation
The Week 3 Data Cleaning and Validation Analysis document contains the detailed methodology, calculations, results, limitations, and execution evidence.

### Conclusion
The project improved data-quality visibility by identifying missing sensor records and introducing record-level quality classification. The original sensor measurements were preserved and verified through an independent integrity check.

### Author

Arokia Bennedict Ebenezar