# Kestra Taxi Data Pipeline – Homework

## Overview
This repository contains a Kestra workflow used to process NYC Taxi data.
The existing pipeline was extended to include data for the year 2021.

Both Green and Yellow taxi datasets were processed.

---

## Dataset
Source:
https://github.com/DataTalksClub/nyc-tlc-data/releases/tag/green/download

Files follow the naming pattern:
- green_tripdata_YYYY-MM.csv
- yellow_tripdata_YYYY-MM.csv

---

## Pipeline Inputs
The flow accepts the following inputs:
- taxi: taxi type (`green` or `yellow`)
- year: year of the dataset
- month: month of the dataset

These inputs are used to dynamically construct the dataset filename and download URL.

---

## 2021 Data Processing
The pipeline was executed using Kestra’s **Schedule trigger** with backfill.

Backfill configuration:
- Trigger type: Schedule
- Backfill period: **2021-01-01 to 2021-07-31**

The backfill was executed separately for each taxi type:
- taxi = green
- taxi = yellow

This ensured that all available monthly datasets for 2021 were processed automatically.

---

## Scheduling
The flow is scheduled using Kestra’s Schedule trigger and supports backfilling.
Timezone configuration follows IANA standards (`America/New_York`).

---

## Notes
This project demonstrates:
- Workflow orchestration using Kestra
- Parameterized flows using inputs and variables
- Backfilling historical data efficiently
