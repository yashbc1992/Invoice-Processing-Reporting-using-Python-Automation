import pytesseract
from PIL import Image

# IMPORTANT: set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load image
img = Image.open("sample_invoice.png")

# Extract text
text = pytesseract.image_to_string(img)

print("Extracted Text:")
print("----------------")
print(text)
