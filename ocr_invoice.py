import os
print("Current working directory:", os.getcwd())
import cv2
import pytesseract

# Set tesseract path (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = cv2.imread(
    r"C:\Users\yashb\Documents\invoice_automation_project\images\invoice_sample.png")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Improve contrast
processed = cv2.adaptiveThreshold(
    gray, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11, 2
)

# Extract text using OCR
text = pytesseract.image_to_string(processed)

# Save OCR output
with open("ocr_output.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("OCR completed. Text saved to ocr_output.txt")
