import fitz
import easyocr
from PIL import Image
import io

# Load EasyOCR once
reader = easyocr.Reader(['en'], gpu=False)


def extract_text_from_pdf(pdf_path):
    text = ""

    doc = fitz.open(pdf_path)

    for page in doc:

        # First try normal PDF text extraction
        page_text = page.get_text("text")

        if page_text.strip():
            text += page_text + "\n"
            continue

        # OCR for scanned pages
        try:
            pix = page.get_pixmap(dpi=300)

            img_bytes = pix.tobytes("png")

            image = Image.open(io.BytesIO(img_bytes))

            results = reader.readtext(image)

            for result in results:
                text += result[1] + " "

            text += "\n"

        except Exception as e:
            print("EasyOCR Error:", e)

    doc.close()

    print("=" * 60)
    print("TEXT LENGTH:", len(text))
    print("TEXT SAMPLE:")
    print(text[:1000])
    print("=" * 60)

    return text