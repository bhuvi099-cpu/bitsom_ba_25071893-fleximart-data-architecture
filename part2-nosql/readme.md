# Part 2: NoSQL Database Analysis

## Objective
This part of the assignment focuses on evaluating the suitability of a
**NoSQL database (MongoDB)** for managing a highly diverse and evolving product
catalog at FlexiMart.

The objective is to analyze the limitations of relational databases for this
use case and demonstrate basic MongoDB operations.

---

## Problem Overview
As FlexiMart expands its product catalog, products begin to vary significantly
in structure and attributes. This creates challenges for traditional relational
databases, which rely on fixed schemas.

This section explores whether MongoDB is a better alternative and demonstrates
its capabilities through theory and practical operations.

---

## Tasks Covered

### Task 2.1: NoSQL Justification Report
Documented in `nosql_analysis.md`.

This report includes:
- Limitations of relational databases when handling diverse product data
- Benefits of MongoDB such as schema flexibility and embedded documents
- Trade-offs and disadvantages of using MongoDB instead of MySQL/PostgreSQL

The report follows the required word limits and is structured into three
clearly defined sections.

---

### Task 2.2: MongoDB Implementation
Implemented in `mongodb_operations.js`.

This task demonstrates:
- Loading JSON data into MongoDB
- Querying products using filters and projections
- Aggregation on nested review data
- Updating documents by adding embedded reviews
- Performing complex aggregation for analytical insights

Sample product data is provided in `products_catalog.json`.

---

## Files in This Folder
- `nosql_analysis.md` – Theory report covering RDBMS limitations, MongoDB benefits, and trade-offs
- `mongodb_operations.js` – MongoDB queries and operations with comments
- `products_catalog.json` – Sample product catalog data in JSON format

---

## Notes
- This part includes both **theory and practical components**
- No MongoDB setup or execution is required for academic evaluation
- Emphasis is placed on conceptual understanding and correct MongoDB syntax

---

## Module Reference
Module 2: AI Data Architecture Design and Implementation  
Part 2: NoSQL Database Analysis
