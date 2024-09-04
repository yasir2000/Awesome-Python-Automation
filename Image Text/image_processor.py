from PIL import Image
from pytesseract import pytesseract
from config import Config

class ImageProcessor:
    def __init__(self, path_to_tesseract):
        self.path_to_tesseract = path_to_tesseract
        self.setup_tesseract()

    def setup_tesseract(self):
        pytesseract.tesseract_cmd = self.path_to_tesseract

    def process_image(self, image_path):
        img = Image.open(image_path)
        return pytesseract.image_to_string(img)

