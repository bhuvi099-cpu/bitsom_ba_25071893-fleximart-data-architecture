# Part 1: Database Design and ETL Pipeline

## Objective
This part of the assignment focuses on building a **complete ETL pipeline**
to process raw CSV data with quality issues, load it into a relational database,
document the database design, and answer business questions using SQL.

The goal is to demonstrate understanding of **data cleaning, relational modeling,
and analytical querying**.

---

## Problem Overview
FlexiMart provides three raw CSV files containing customer, product, and sales
data. These files include intentional data quality issues such as missing values,
duplicates, and inconsistent formats.

The task is to clean this data, load it into a structured database using a
provided schema, and generate meaningful business insights.

---

## Data Files
The following input files are used:

- `customers_raw.csv`  
  Issues include missing emails, duplicate records, and inconsistent phone formats.

- `products_raw.csv`  
  Issues include missing prices, inconsistent category naming, and null stock values.

- `sales_raw.csv`  
  Issues include missing customer/product IDs, duplicate transactions, and
  inconsistent date formats.

All files are located in the root `data/` directory.

---

## Tasks Covered

### Task 1.1: ETL Pipeline Implementation
Implemented in `etl_pipeline.py`.

This script performs:
- **Extract:** Reads all three CSV files
- **Transform:**
  - Removes duplicate records
  - Handles missing values using appropriate strategies
  - Standardizes phone number formats
  - Standardizes product category names
  - Converts dates to `YYYY-MM-DD` format
  - Uses surrogate keys instead of business IDs
- **Load:** Inserts cleaned data into a MySQL/PostgreSQL database using the
  provided schema

A data quality summary is generated as `data_quality_report.txt`.

---

### Task 1.2: Database Schema Documentation
Implemented in `schema_documentation.md`.

This document includes:
- Text-based entity descriptions for all tables
- Explanation of relationships between entities
- Justification of Third Normal Form (3NF)
- Identification of functional dependencies
- Sample data representation for each table

---

### Task 1.3: Business Query Implementation
Implemented in `business_queries.sql`.

This file contains SQL queries answering:
1. Customer purchase history analysis
2. Product category sales analysis
3. Monthly sales trend analysis for 2024

Each query uses proper joins, aggregation, filtering, and ordering as required.

---

## Files in This Folder
- `etl_pipeline.py` – ETL pipeline implementation
- `data_quality_report.txt` – Summary of data cleaning results
- `schema_documentation.md` – Database design and normalization documentation
- `business_queries.sql` – SQL queries answering business scenarios

---

## Notes
- The database schema is used **exactly as provided** in the assignment
- This part focuses on **relational data processing and analytics**
- Code execution is not required for academic evaluation
- Emphasis is placed on correctness, clarity, and design logic

---

## Module Reference
Module 2: AI Data Architecture Design and Implementation  
Part 1: Database Design and ETL Pipeline
