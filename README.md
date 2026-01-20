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

## How to Run the Project
```bash
pip install opencv-python pytesseract


## Ensure Tesseract is installed and path is configured:
```bash
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

##Run OCR:
```bash
python ocr_invoice.py


##Extract fields:
```bash
python extract_invoice_fields.py

1️⃣ What is pytesseract?
pytesseract is a Python wrapper for Tesseract OCR.
Tesseract = the actual OCR engine (software that reads text from images)
pytesseract = Python library that talks to Tesseract for you

Python cannot do OCR by itself, so it uses Tesseract through pytesseract.
OCR = Optical Character Recognition

👉 Converts:

Image (PNG / JPG / Screenshot)
        ↓
Editable Text

3️⃣ Why do we need BOTH?
🔹 Tesseract (installed software) is installed on our system.it does the actual text recognition,written in C++.

🔹 pytesseract (Python library) Sends image to Tesseract,gets text back into Python,makes OCR usable inside Python scripts.

📌 Think like this:

Tesseract = Engine
pytesseract = Steering wheel

4️⃣ Why do we need to set this line?
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

Reason:Windows does not always know where Tesseract is installed.

So we explicitly tell Python:“Hey, OCR engine is here”

Without this:
Python will say: ❌ Tesseract not found

5️⃣ What does this line do?
text = pytesseract.image_to_string(processed)


This is the core OCR step 🔥

What happens internally:

Python sends the image to Tesseract

Tesseract reads letters from the image

Tesseract returns detected text

Python stores it in text

📌 Output is plain string

6️⃣ Why did we use OpenCV before pytesseract?

OCR accuracy depends on image quality

So we did:

*Convert to grayscale

*Improve contrast

*Remove noise

This helps Tesseract to read text more accurately

Pipeline:

Image
  ↓ (OpenCV)
Preprocessed Image
  ↓ (pytesseract)
Extracted Text

7️⃣ Why pytesseract is useful?

Because it shows:

*Real-world automation

*Document processing

*OCR + Python integration

Used in tools like Kofax, UiPath, ABBYY

This is industry-relevant, not just theory.

8️⃣ One-line explanation: pytesseract is a Python wrapper that allows Python programs to use the Tesseract OCR engine to extract text from images and scanned documents.