import os

CSV_FILE = "output/all_invoices_report.csv"
ERROR_LOG = "error/errors.log"

total_invoices = 0
processed_count = 0
error_count = 0

# count invoice txt files
for file in os.listdir("."):
    if file.startswith("invoice") and file.endswith(".txt"):
        total_invoices += 1

# count processed invoices from CSV
if os.path.exists(CSV_FILE):
    with open(CSV_FILE, "r") as f:
        processed_count = len(f.readlines()) - 1  # minus header

# count error invoices from log
if os.path.exists(ERROR_LOG):
    with open(ERROR_LOG, "r") as f:
        error_count = len([
            line for line in f.readlines()
            if line.strip().startswith("invoice")
        ])

print("\nInvoice Processing Summary")
print("--------------------------")
print("Total invoices:", total_invoices)
print("Processed (valid):", processed_count)
print("Errors:", error_count)
