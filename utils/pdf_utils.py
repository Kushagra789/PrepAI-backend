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

            # -----------------------------
            # 1. NORMAL PDF TEXT EXTRACTION
            # -----------------------------
            page_text = page.get_text("text")

            if page_text and page_text.strip():
                text += page_text + "\n"

            # -----------------------------
            # 2. OCR FOR SCANNED PDF
            # -----------------------------
            else:
                try:
                    # HIGH RESOLUTION (IMPORTANT FOR ACCURACY)
                    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3))

                    img_data = pix.tobytes("png")
                    image = Image.open(io.BytesIO(img_data))

                    # OCR CONFIG (improves detection)
                    custom_config = r'--oem 3 --psm 6'

                    ocr_text = pytesseract.image_to_string(
                        image,
                        config=custom_config
                    )

                    text += ocr_text + "\n"

                except Exception as ocr_error:
                    print("OCR error:", ocr_error)

        document.close()

    except Exception as e:
        print("PDF extraction error:", e)
        print("EXTRACTED TEXT:", text[:1000])

    return text