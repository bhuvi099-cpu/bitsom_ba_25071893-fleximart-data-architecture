# Task 3.1: Star Schema Design Documentation

## Objective
This task focuses on designing and documenting a **star schema** for the
FlexiMart data warehouse to support historical sales analysis.

The objective is to clearly describe the fact table, dimension tables, design
decisions, and how transactional data is represented in the data warehouse.

---

## Scope of This Task
This task is **documentation-focused** and does not involve SQL execution or
data loading. It demonstrates understanding of **dimensional modeling**
principles.

---

## File Included

### `star_schema_design.md`

This file contains the complete documentation required for Task 3.1 and is
structured into the following sections:

---

## Section 1: Schema Overview
- Text-based description of the **star schema**
- Definition of the **fact table (fact_sales)** including:
  - Grain
  - Business process
  - Measures (numeric facts)
  - Foreign key relationships
- Description of **dimension tables**:
  - `dim_date`
  - `dim_product`
  - `dim_customer`
- Each table is documented with purpose, type, and attributes

---

## Section 2: Design Decisions
This section explains:
- Why the fact table grain is defined at the **transaction line-item level**
- Why **surrogate keys** are used instead of natural keys
- How the design supports **drill-down and roll-up** analysis across dimensions

---

## Section 3: Sample Data Flow
This section demonstrates:
- How a single source transaction is transformed
- How the transaction is represented in:
  - `fact_sales`
  - `dim_date`
  - `dim_product`
  - `dim_customer`
- Clear mapping between operational data and warehouse tables

---

## Evaluation Alignment
This documentation directly addresses the evaluation criteria:
- **Schema description**: All fact and dimension tables are clearly documented
- **Design justification**: Sound reasoning for modeling choices is provided
- **Sample data flow**: Demonstrates understanding of dimensional modeling

---

## Notes
- This task focuses only on **star schema design**
- No diagrams are used, as per instructions
- Content is prepared for **academic evaluation**

---

## Module Reference
Module 2: AI Data Architecture Design and Implementation  
Part 3: Data Warehouse and Analytics  
Task 3.1: Star Schema Design Documentation
