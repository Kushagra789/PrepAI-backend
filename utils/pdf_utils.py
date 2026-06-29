import fitz
import pytesseract
from PIL import Image
import io
import os

if os.name == "nt":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_pdf(pdf_path):
    text = ""

    doc = fitz.open(pdf_path)

    for page in doc:

        # STEP 1: try normal text
        page_text = page.get_text("text")
        if page_text and page_text.strip():
            text += page_text + "\n"
            continue

        # STEP 2: better OCR pipeline
        pix = page.get_pixmap(dpi=300)  # IMPORTANT FIX (use dpi instead of matrix)

        img_bytes = pix.tobytes("png")
        image = Image.open(io.BytesIO(img_bytes))

        # convert to grayscale (IMPORTANT for OCR accuracy)
        image = image.convert("L")

        # OCR config (VERY IMPORTANT)
        custom_config = r'--oem 3 --psm 6'

        ocr_text = pytesseract.image_to_string(image, config=custom_config)

        text += ocr_text + "\n"

    doc.close()

    return text