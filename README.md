# green_taxi_etl pipeline

## Overview
This project implements an ETL pipeline that processes NYC Green Taxi trip data
for October, November, and December 2020. The pipeline extracts data from a public
GitHub source, transforms it using Pandas, and loads it into Postgres and Google
Cloud Storage.

---

## Dataset
Source:
https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/green/download

Files used:
- green_tripdata_2020-10.csv.gz
- green_tripdata_2020-11.csv.gz
- green_tripdata_2020-12.csv.gz

---

## ETL Steps

### Extract
- Data is downloaded using Pandas
- Only Q4 2020 (Oct–Dec) files are loaded
- Files are concatenated using a for-loop and `pd.concat`

### Transform
- Rows with `passenger_count = 0` or `trip_distance = 0` are removed
- A new column `lpep_pickup_date` is created from `lpep_pickup_datetime`
- Column names are converted from CamelCase to snake_case
- Assertions ensure data quality

### Load
- Data is written to Postgres in the `mage.green_taxi` table
- Table is replaced if it already exists

### Export
- Data is written to Google Cloud Storage as Parquet files
- Files are partitioned by `lpep_pickup_date`

---

## Scheduling
The pipeline is scheduled to run daily at 5:00 AM UTC using a cron job.

---

## Homework Questions

### Question 1
**Once the dataset is loaded, what's the shape of the data?**

Answer: **544,898 rows × 20 columns**

---

### Question 2
**How many rows remain after filtering passenger_count > 0 and trip_distance > 0?**

Answer: **266,855 rows**

---

### Question 3
**How is `lpep_pickup_date` created?**

Answer:
```python
data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

Question 4

What are the existing values of VendorID?

Answer: 1 or 2

Question 5

How many columns are renamed to snake case?

Answer: 4

Question 6

How many partitions are created in Google Cloud Storage?

Answer: 96
