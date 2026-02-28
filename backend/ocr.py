import pytesseract
from PIL import Image

# Change path if different in your system
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(image_file):
    image = Image.open(image_file)
    text = pytesseract.image_to_string(image)
    return text