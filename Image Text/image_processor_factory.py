from config import Config
from image_processor import ImageProcessor

class ImageProcessorFactory:
    @staticmethod
    def create_image_processor():
        tesseract_path = Config.get_path_to_tesseract()
        return ImageProcessor(tesseract_path)
