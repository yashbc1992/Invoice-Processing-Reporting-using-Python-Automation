import re
from pathlib import Path

# Read OCR text
text_path = Path("output/ocr_text_from_contrast.txt")
text = text_path.read_text()

data = {}

# Extract fields using regex
data["invoice_number"] = re.search(r"Invoice Number:\s*(.*)", text).group(1)
data["customer_name"] = re.search(r"Customer Name:\s*(.*)", text).group(1)
data["invoice_date"] = re.search(r"Invoice Date:\s*(.*)", text).group(1)
data["total_amount"] = re.search(r"Total Amount:\s*(\d+)", text).group(1)

# Extract items
items = re.findall(r"(\w+)\s+(\d+)\s+(\d+)", text)
data["items"] = [
    {"item": i[0], "quantity": i[1], "price": i[2]} for i in items
]

print("Extracted Invoice Data")
print("----------------------")
for k, v in data.items():
    print(f"{k}: {v}")
