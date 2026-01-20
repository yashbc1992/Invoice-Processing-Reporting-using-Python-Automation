from PIL import Image, ImageEnhance
import os

# Paths
INPUT_IMAGE = "output/sample_invoice_gray.png"
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load grayscale image
img = Image.open(INPUT_IMAGE)

# Improve contrast
enhancer = ImageEnhance.Contrast(img)
contrast_img = enhancer.enhance(2.0)  # 2.0 = stronger contrast

# Save result
output_path = os.path.join(OUTPUT_DIR, "sample_invoice_contrast.png")
contrast_img.save(output_path)

print("✅ Contrast improved")
print(f"Saved at: {output_path}")
