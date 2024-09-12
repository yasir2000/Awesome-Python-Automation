import os

class Config:
    @staticmethod
    def get_path_to_tesseract():
        return os.getenv("TESSERACT_PATH", r"G:\Program Files\Tesseract-OCR\tesseract.exe")

    @staticmethod
    def get_image_path():
        return os.getenv("IMAGE_PATH", r"C:\Users\yasirkaram\Downloads\image3.png")
