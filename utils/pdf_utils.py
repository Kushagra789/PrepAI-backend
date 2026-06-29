import fitz
import pytesseract
from PIL import Image
import io
import os

# Windows only
if os.name == "nt":
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )


def extract_text_from_pdf(pdf_path):
    text = ""

    doc = fitz.open(pdf_path)

    for page in doc:

        # Try normal PDF text first
        page_text = page.get_text("text")

        if page_text.strip():
            text += page_text + "\n"

        else:
            # Skip OCR on Render/Linux because Tesseract isn't installed
            if os.name == "nt":
                try:
                    pix = page.get_pixmap(dpi=300)

                    img = Image.open(io.BytesIO(pix.tobytes("png")))
                    img = img.convert("L")

                    ocr = pytesseract.image_to_string(img)

                    text += ocr + "\n"

                except Exception as e:
                    print("OCR Error:", e)

    doc.close()

    print("=" * 60)
    print("TEXT LENGTH:", len(text))
    print("TEXT SAMPLE:")
    print(text[:1000])
    print("=" * 60)

    return text