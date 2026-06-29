import fitz
import pytesseract
from PIL import Image
import io
import os

# Windows only
if os.name == "nt":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_pdf(pdf_path):
    text = ""

    doc = fitz.open(pdf_path)

    for page in doc:

        try:
            # STEP 1: normal text extraction
            page_text = page.get_text("text")
            if page_text and page_text.strip():
                text += page_text + "\n"
                continue

            # STEP 2: OCR fallback (SAFE)
            pix = page.get_pixmap(dpi=200)  # reduced for stability

            img_bytes = pix.tobytes("png")
            image = Image.open(io.BytesIO(img_bytes))

            image = image.convert("L")

            custom_config = r'--oem 3 --psm 6'

            # SAFE OCR (won't crash backend)
            try:
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                text += ocr_text + "\n"
            except Exception:
                text += ""

        except Exception:
            # if anything fails → skip page safely
            continue

    doc.close()

    return text