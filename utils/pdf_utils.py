import fitz
import pytesseract
from PIL import Image
import io
import os

# Set Windows path only when running on Windows
if os.name == "nt":
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )


def extract_text_from_pdf(pdf_path):
    text = ""

    document = fitz.open(pdf_path)

    for page in document:
        page_text = page.get_text()

        # PDF already contains selectable text
        if page_text.strip():
            text += page_text

        # Scanned PDF → OCR
        else:
            try:
                pix = page.get_pixmap()
                image = Image.open(io.BytesIO(pix.tobytes("png")))
                text += pytesseract.image_to_string(image)
            except Exception:
                pass

    document.close()

    return text