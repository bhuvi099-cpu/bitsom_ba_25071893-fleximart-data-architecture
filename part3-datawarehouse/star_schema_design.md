# Task 3.1: Star Schema Design

## Objective
This task focuses on designing a **star schema** for the FlexiMart data
warehouse to support historical sales analysis and analytical reporting.

The objective is to clearly define the fact table, dimension tables, and the
design logic behind the schema.

---

## What This Task Covers
- Identification of the business process (sales transactions)
- Definition of fact table grain and measures
- Description of dimension tables (date, product, customer)
- Justification of design decisions
- Illustration of data flow from source to data warehouse

---

## File Included

- `star_schema_design.md`  
  This file contains:
  - Text-based description of the star schema
  - Fact and dimension table definitions
  - Design decisions such as granularity and surrogate keys
  - Example of how a sales transaction is represented in the data warehouse

---

## Design Approach
- A **fact table** is used to store measurable sales data
- **Dimension tables** store descriptive attributes for analysis
- **Surrogate keys** are used to improve performance and maintain consistency
- The schema supports **drill-down and roll-up** operations across time,
  products, and customers

---

## Notes
- This task is focused on **data warehouse design**, not ETL or implementation
- No code execution is required
- Content is prepared for academic evaluation

---

## Module Reference
Module 2: AI Data Architecture Design and Implementation  
Part 3: Data Warehouse and Analytics
