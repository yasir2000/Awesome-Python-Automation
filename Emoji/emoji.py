import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


# Environment Variable Configuration
class Config:
    @staticmethod
    def get_output_filename():
        return os.getenv("PDF_OUTPUT_FILENAME", "emoji.pdf")

    @staticmethod
    def get_emoji():
        return os.getenv("PDF_EMOJI", "😊")

    @staticmethod
    def get_font_path():
        return os.getenv("PDF_FONT_PATH", "emoji.tiff")


# Abstract Factory
class PDFFactory:
    def create_canvas(self):
        return canvas.Canvas(Config.get_output_filename(), pagesize=letter)


# Builder
class PDFBuilder:
    def __init__(self, factory: PDFFactory):
        self.canvas = factory.create_canvas()

    def register_font(self, font_path):
        pdfmetrics.registerFont(TTFont('EmojiFont', font_path))

    def add_emoji(self, emoji):
        self.canvas.setFont('EmojiFont', 36)
        self.canvas.drawString(100, 400, emoji)

    def save_pdf(self):
        self.canvas.save()


# Command Pattern
class CreatePDFCommand:
    def __init__(self, builder: PDFBuilder, emoji):
        self.builder = builder
        self.emoji = emoji

    def execute(self):
        self.builder.register_font(Config.get_font_path())
        self.builder.add_emoji(self.emoji)
        self.builder.save_pdf()


# Main execution
if __name__ == "__main__":
    output_filename = Config.get_output_filename()
    emoji = Config.get_emoji()
    font_path = Config.get_font_path()

    # Inversion of Control through Dependency Injection
    factory = PDFFactory()
    builder = PDFBuilder(factory)
    command = CreatePDFCommand(builder, emoji)
    
    command.execute()
