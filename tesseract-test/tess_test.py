from PIL import Image
import pytesseract

def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    boxes = pytesseract.image_to_data(Image.open(filename))
    return boxes

#pytesseract.pytesseract.tesseract_cmd = r"/home/akshay/.local/share/virtualenvs/cmpe273-assignment2-K-Pb6TPb/bin/pytesseract"
print(ocr_core('sample-scantron.jpg'))
