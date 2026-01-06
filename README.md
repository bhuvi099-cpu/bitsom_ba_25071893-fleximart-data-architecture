# fleximart-data-pipeline
ETL pipeline and database design for FlexiMart e-commerce analytics
# FlexiMart – Data Architecture & ETL Pipeline

## Course
**Data for Artificial Intelligence**  
Module 2 – Assignment: AI Data Architecture Design and Implementation

## Assignment Context
This project is an individual assignment that simulates a real-world **Data Engineer** role at **FlexiMart**, an e-commerce company.  
The objective is to design and document a complete **data pipeline** that ingests raw data, resolves data quality issues, stores it in a relational database, and enables analytical reporting.

The focus of this submission is on **data architecture design, ETL logic, SQL analytics, and documentation**, as required by the assignment.

---

## Project Objectives
- Build an ETL pipeline to process raw CSV data
- Handle real-world data quality issues
- Load cleaned data into a normalized relational database
- Document database design and normalization
- Answer business questions using SQL

---

## Repository Structure
fleximart-data-pipeline/
│
├── etl_pipeline.py
├── data_quality_report.txt
├── schema_documentation.md
├── business_queries.sql
│
└── data/
├── customers_raw.csv
├── products_raw.csv
└── sales_raw.csv

yaml
Copy code

---

## Dataset Overview

### Customers (`customers_raw.csv`)
Contains customer demographic and registration information.

**Known data quality issues:**
- Missing email values
- Duplicate customer records
- Inconsistent phone number formats
- Inconsistent date formats
- Mixed case city names

---

### Products (`products_raw.csv`)
Contains product catalog information.

**Known data quality issues:**
- Missing product prices
- Inconsistent category naming (case variations)
- Missing stock quantities

---

### Sales (`sales_raw.csv`)
Contains transactional sales data.

**Known data quality issues:**
- Duplicate transactions
- Missing customer or product IDs
- Inconsistent date formats

All data quality issues are intentionally included as part of the assignment requirements.

---

## ETL Pipeline (`etl_pipeline.py`)

The ETL pipeline is implemented in Python and follows three stages:

### 1. Extract
- Reads all raw CSV files using pandas

### 2. Transform
- Removes duplicate records
- Handles missing values using appropriate strategies (drop, fill, default)
- Standardizes phone numbers to Indian format: `+91-XXXXXXXXXX`
- Standardizes product category names
- Converts all date fields to ISO format (`YYYY-MM-DD`)
- Drops business identifiers and relies on surrogate keys (auto-increment IDs)

### 3. Load
- Loads cleaned data into a relational database
- Uses the **exact schema provided in the assignment**
- Populates the following tables:
  - customers
  - products
  - orders
  - order_items

---

## Data Quality Report
The file `data_quality_report.txt` summarizes:
- Number of records processed per dataset
- Number of duplicate records removed
- Number of missing values handled
- Number of records successfully loaded

This report demonstrates transparency and traceability of the ETL process.

---

## Database Design Documentation
The database schema and design decisions are documented in `schema_documentation.md`, including:
- Entity descriptions
- Table attributes
- Relationships between entities
- Third Normal Form (3NF) justification
- Sample data representation

---

## Business Queries
The file `business_queries.sql` contains SQL queries answering key business questions:
1. Customer purchase history analysis
2. Product category sales analysis
3. Monthly sales trends with cumulative revenue

All queries strictly follow the requirements specified in the assignment and use appropriate joins, aggregations, and filtering.

---

## Assumptions & Notes
- This repository is submitted **for academic evaluation via GitHub**
- Code execution is **not required as part of submission**
- The ETL script is designed to be compatible with **MySQL or PostgreSQL**
- Emphasis is placed on **correctness of logic, clarity of design, and documentation quality**

---

## Submission Details
- Assignment Type: Individual Project
- Submission Mode: GitHub Repository
- Estimated Effort: ~10 hours

---
