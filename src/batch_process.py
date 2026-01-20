import os
from datetime import datetime

BASE_DIR = os.getcwd()
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
ERROR_DIR = os.path.join(BASE_DIR, "error")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(ERROR_DIR, exist_ok=True)

csv_path = os.path.join(OUTPUT_DIR, "all_invoices_report.csv")
error_log_path = os.path.join(ERROR_DIR, "errors.log")

with open(csv_path, "w") as csv_file, open(error_log_path, "w") as error_log:
    csv_file.write("File,Invoice Number,Customer,Amount,Status,Processed At\n")
    error_log.write(f"Error log - {datetime.now()}\n")
    error_log.write("=" * 60 + "\n")

    for filename in os.listdir(BASE_DIR):
        if not filename.endswith(".txt"):
            continue

        if filename.startswith("invoice"):
            file_path = os.path.join(BASE_DIR, filename)

            invoice_number = ""
            customer = ""
            amount = None
            errors = []

            with open(file_path, "r") as f:
                for line in f:
                    if "Invoice Number" in line:
                        invoice_number = line.split(":")[1].strip()
                    elif "Customer" in line:
                        customer = line.split(":")[1].strip()
                    elif "Amount" in line:
                        value = line.split(":")[1].strip()
                        if value.isdigit():
                            amount = int(value)
                        else:
                            errors.append(f"Amount is not a valid number: '{value}'")

            if amount is None:
                errors.append("Missing Amount")

            if errors:
                error_log.write(f"\n{filename}\n")
                for e in errors:
                    error_log.write(f"  - {e}\n")
                continue

            status = "APPROVED" if amount >= 3000 else "REVIEW"
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            csv_file.write(
                f"{filename},{invoice_number},{customer},{amount},{status},{timestamp}\n"
            )

print("✔ Batch invoice processing completed")
