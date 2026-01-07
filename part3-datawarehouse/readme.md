# Part 3: Data Warehouse and Analytics

## Objective
This section addresses **Part 3 of the assignment**, which focuses on designing
a **data warehouse** for FlexiMart to analyze **historical sales patterns** and
generate analytical reports for business decision-making.

The goal is to model data in a form optimized for analytics rather than
transactional processing.

---

## Problem Context
FlexiMart requires a centralized data warehouse that enables:
- Trend analysis over time
- Product and customer performance analysis
- Management-level reporting and insights

To meet these requirements, a **star schema** data warehouse design is used,
along with OLAP-style analytical SQL queries.

---

## Scope of This Section
This part includes:

1. **Star Schema Design Documentation**
   - Definition of fact and dimension tables
   - Explanation of design decisions
   - Sample data flow from source to warehouse

2. **Star Schema Implementation**
   - SQL schema creation using a provided warehouse schema
   - Insertion of realistic dimensional and fact data

3. **OLAP Analytics Queries**
   - Drill-down analysis by time (Year → Quarter → Month)
   - Product performance analysis
   - Customer segmentation analysis

---

## Files Included

- `star_schema_design.md`  
  Documents the star schema design, including grain, measures, dimensions,
  design justification, and sample data flow.

- `warehouse_schema.sql`  
  Contains SQL statements to create all dimension and fact tables using the
  **exact schema provided** in the assignment.

- `warehouse_data.sql`  
  Populates the data warehouse with realistic sample data, meeting minimum
  volume and data quality requirements.

- `analytics_queries.sql`  
  Contains OLAP-style SQL queries that answer specific business scenarios using
  aggregation, grouping, and analytical functions.

---

## Data Warehouse Design Approach
- **Star schema** is used for simplicity and query performance
- **Fact table** captures measurable sales data
- **Dimension tables** provide descriptive context (date, product, customer)
- **Surrogate keys** are used for efficient joins and historical tracking

---

## Analytical Capabilities Demonstrated
- Time-based drill-down and roll-up analysis
- Revenue and quantity aggregation
- Top-N product analysis with percentage contribution
- Customer value segmentation using CASE logic

---

## Assumptions
- Data warehouse is populated from cleaned transactional data
- This section focuses on **analytics and reporting**, not ETL pipelines
- SQL scripts are intended for academic evaluation and may not be executed
  as part of submission

---

## Module Reference
Module 2: AI Data Architecture Design and Implementation  
Part 3: Data Warehouse and Analytics
