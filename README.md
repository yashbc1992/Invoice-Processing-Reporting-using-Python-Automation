# Invoice Automation Project (Python)

## Description
Python script that batch-processes invoice text files, validates data,
applies approval rules, and generates CSV reports and error logs.

## What it does
- Reads invoice `.txt` files
- Extracts Invoice Number, Customer, Amount
- Handles invalid or missing data
- Approves invoices >= 3000
- Generates:
  - CSV summary report
  - Error log for failed invoices

## How to run
```bash
python batch_process.py
