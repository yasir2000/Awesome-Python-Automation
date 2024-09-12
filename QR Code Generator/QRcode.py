import os
from dotenv import load_dotenv
import qrcode

load_dotenv()  # Load environment variables

# Configuration and constants retrieval
QR_CONTENT = os.getenv("QR_CONTENT")
QR_VERSION = int(os.getenv("QR_VERSION"))
QR_ERROR_CORRECTION = int(os.getenv("QR_ERROR_CORRECTION"))
QR_FILL_COLOR = os.getenv("QR_FILL_COLOR")
QR_BACK_COLOR = os.getenv("QR_BACK_COLOR")
QR_IMAGE_NAME = os.getenv("QR_IMAGE_NAME")

# Builder Pattern for QR Code Configuration
class QRCodeBuilder:
    def __init__(self):
        self.qr_code = qrcode.QRCode(
            version=QR_VERSION,
            error_correction=QR_ERROR_CORRECTION
        )
    
    def add_data(self, data):
        self.qr_code.add_data(data)
        self.qr_code.make(fit=True)
        return self
    
    def build_image(self, fill_color=QR_FILL_COLOR, back_color=QR_BACK_COLOR):
        return self.qr_code.make_image(fill_color=fill_color, back_color=back_color)

# Singleton Pattern to ensure a single QR code generator instance
class QRCodeGenerator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(QRCodeGenerator, cls).__new__(cls)
        return cls._instance

    def generate_qr_code(self, content):
        builder = QRCodeBuilder()
        return builder.add_data(content).build_image()

# Facade to simplify the QR code creation process
class QRCodeFacade:
    def __init__(self, content):
        self.content = content
        self.generator = QRCodeGenerator()

    def create_and_save_qr(self, image_name):
        img = self.generator.generate_qr_code(self.content)
        img.save(image_name)

# Main execution
if __name__ == "__main__":
    qr_facade = QRCodeFacade(QR_CONTENT)
    qr_facade.create_and_save_qr(QR_IMAGE_NAME)
