# ETL Logging & Monitoring

## Project focus
Add simple operational visibility to recurring data loads so failures, partial loads, and row-count differences are easier to diagnose.

## What is tracked
- Run start and end time
- Source file or process name
- Status such as SUCCESS / FAILED / PARTIAL
- Rows read and loaded
- Validation result
- Error message or exception details
- Reconciliation summary

## Workflow
1. Run the ETL process.
2. Capture run metadata.
3. Validate the load.
4. Store status and row counts.
5. Record errors and exceptions.
6. Use the log for troubleshooting and reporting.

## Tools
Python · PostgreSQL · SQL · ETL · Logging · Data Quality

> Portfolio examples use sample or anonymized data only.
