# CSV to PostgreSQL ETL

## Project focus
Automate loading structured CSV data into PostgreSQL with repeatable validation and clear failure handling.

## Typical workflow
1. Read one or more CSV files.
2. Validate required columns and data types.
3. Clean invalid values where appropriate.
4. Load the data into staging or target PostgreSQL tables.
5. Reconcile source and loaded row counts.
6. Record the result in a log.

## Useful features
- Repeatable imports
- Schema and column checks
- Data type conversion
- Duplicate detection
- Source file tracking
- Row-count reconciliation
- Error logging

## Tools
Python · pandas · PostgreSQL · SQL · ETL · Data Validation

> Portfolio examples use sample or anonymized data only.
