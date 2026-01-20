import os

ERROR_LOG_PATH = os.path.join("output", "errors.log")

if not os.path.exists(ERROR_LOG_PATH):
    print("No errors.log file found")
else:
    print("Invalid Invoices and Reasons")
    print("----------------------------")

    with open(ERROR_LOG_PATH, "r") as f:
        for line in f:
            if line.strip():
                print(line.strip())
