import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
import os

# Windows Tesseract path
if os.name == "nt":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_pdf(pdf_path):
    text = ""

    try:
        document = fitz.open(pdf_path)

        for page in document:
            # 1. Try normal text extraction first
            page_text = page.get_text("text")

            if page_text and page_text.strip():
                text += page_text + "\n"

            else:
                # 2. OCR fallback for scanned PDFs
                pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # better quality image
                img_data = pix.tobytes("png")

                image = Image.open(io.BytesIO(img_data))

                ocr_text = pytesseract.image_to_string(image)

                text += ocr_text + "\n"

        document.close()

    except Exception as e:
        print("PDF extraction error:", e)

    return text