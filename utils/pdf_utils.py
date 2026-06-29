import fitz
import pytesseract
from PIL import Image
import io
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_pdf(pdf_path):
    text = ""

    document = fitz.open(pdf_path)

    for page in document:
        page_text = page.get_text()

        # If PDF already has text
        if page_text.strip():
            text += page_text

        # If PDF is scanned, use OCR
        else:
            pix = page.get_pixmap()

            image = Image.open(io.BytesIO(pix.tobytes("png")))

            ocr_text = pytesseract.image_to_string(image)

            text += ocr_text

    document.close()

    return text