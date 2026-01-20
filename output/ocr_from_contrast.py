import pytesseract
from PIL import Image
import os

# Path to Tesseract (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Input image (contrast-enhanced)
IMAGE_PATH = "output/sample_invoice_contrast.png"

# Output text file
OUTPUT_TEXT = "output/ocr_text_from_contrast.txt"

# Load image
img = Image.open(IMAGE_PATH)

# OCR extraction
text = pytesseract.image_to_string(img, config="--psm 6")

print("===== OCR TEXT (FROM CONTRAST IMAGE) =====")
print(text)

# Save OCR output
with open(OUTPUT_TEXT, "w", encoding="utf-8") as f:
    f.write(text)

print("\n✅ OCR text saved to:", OUTPUT_TEXT)
