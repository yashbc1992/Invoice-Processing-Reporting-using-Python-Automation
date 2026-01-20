from PIL import Image
import os

# Input image
INPUT_IMAGE = "sample_invoice.png"

# Output folder
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load image
img = Image.open(INPUT_IMAGE)

# Convert to grayscale
gray_img = img.convert("L")

# Save grayscale image
output_path = os.path.join(OUTPUT_DIR, "sample_invoice_gray.png")
gray_img.save(output_path)

print("✅ Image converted to grayscale")
print(f"Saved at: {output_path}")
