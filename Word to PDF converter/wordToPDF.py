import os
from docx2pdf import convert
from abc import ABC, abstractmethod
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

class DocumentConverter(ABC):
    @abstractmethod
    def convert(self, word_file_path: str) -> str:
        pass

class PDFConverter(DocumentConverter):
    def convert(self, word_file_path: str) -> str:
        output_pdf_path = os.path.splitext(word_file_path)[0] + ".pdf"
        try:
            convert(word_file_path, output_pdf_path)
            logging.info(f"Conversion successful. PDF saved at {output_pdf_path}")
            return output_pdf_path
        except Exception as e:
            logging.error(f"Error occurred during conversion: {e}")
            return None

class ConversionService:
    def __init__(self, converter: DocumentConverter):
        self.converter = converter
    
    def convert_documents(self, word_file_paths):
        for word_file_path in word_file_paths:
            self.converter.convert(word_file_path)

def main():
    # Set up logging
    logging.basicConfig(level=logging.INFO)

    word_files = [
        os.getenv("WORD_FILE_PATH_1"),
        os.getenv("WORD_FILE_PATH_2"),
        os.getenv("WORD_FILE_PATH_3"),
        os.getenv("WORD_FILE_PATH_4"),
        os.getenv("WORD_FILE_PATH_5"),
        os.getenv("WORD_FILE_PATH_6"),
        os.getenv("WORD_FILE_PATH_7"),
        os.getenv("WORD_FILE_PATH_8"),
        os.getenv("WORD_FILE_PATH_9"),
    ]
    
    # Filter out any None paths
    word_files = [path for path in word_files if path]

    pdf_converter = PDFConverter()
    conversion_service = ConversionService(pdf_converter)
    conversion_service.convert_documents(word_files)

if __name__ == "__main__":
    main()
