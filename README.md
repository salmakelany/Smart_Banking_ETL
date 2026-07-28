# 🏦 Smart Banking ETL Pipeline

This repository contains the ETL (Extract, Transform, Load) pipeline developed for the **Smart Banking Analytics & Fraud Detection System**.

The pipeline is responsible for extracting raw banking data, cleaning and validating it, loading it into PostgreSQL, and populating a Data Warehouse using a Star Schema design.
---
# 📌 Overview
The ETL pipeline consists of three main stages:

- **Extract** – Read raw banking data from CSV files.
- **Transform** – Clean, validate, and standardize the data.
- **Load** – Load the cleaned data into PostgreSQL and populate the Data Warehouse.
---
# 🔄 ETL Workflow

```text
Raw CSV Files
        │
        ▼
Extract
        │
        ▼
Transform
 • Clean Data
 • Remove Duplicates
 • Validate Keys
 • Convert Data Types
        │
        ▼
Load to PostgreSQL
        │
        ▼
Dimension Tables
        │
        ▼
Fact Table
        │
        ▼
Data Warehouse
```

---
# 📂 Project Structure
```text
scripts/
│
├── extract.py
├── transform.py
├── check_columns.py
├── quality_checks.py
├── load.py
├── load_dw.py
├── load_fact.py
└── config.py

data/
cleaned_data/
```
---
# 📁 Script Responsibilities
### extract.py
Reads all CSV files and loads them into Pandas DataFrames.

### transform.py
Performs data cleaning and transformation including:

- Column normalization
- Data type conversion
- Duplicate removal
- Missing value normalization
- Primary Key validation
- Foreign Key validation

### check_columns.py
Verifies that all required columns exist before loading.

### quality_checks.py
Runs data quality checks to ensure data consistency and integrity.

### load.py
Loads cleaned data into PostgreSQL source tables.

### load_dw.py
Builds and populates Dimension Tables inside the Data Warehouse.

### load_fact.py
Creates and loads the Fact Table by integrating transactional and dimensional data.

### config.py
Stores centralized ETL configuration such as table metadata, keys, date columns, and loading order.

---
# 🛠 Technologies Used
- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- pgAdmin 4

---
# 📊 Data Warehouse
The Data Warehouse follows a **Star Schema** architecture consisting of:

- DimCustomer
- DimBranch
- DimAccount
- DimEmployee
- DimLoan
- DimDate
- Fact_Transactions

---
# 🚀 Key ETL Features

- Automated CSV extraction
- Data cleaning and preprocessing
- Duplicate removal
- Primary & Foreign Key validation
- PostgreSQL integration
- Data Warehouse population
- Star Schema implementation

---
# 👩‍💻 Author
**Salma Kelany**
ETL & Data Engineering
