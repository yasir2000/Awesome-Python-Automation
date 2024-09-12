import os
import argparse
import pdfkit
from abc import ABC, abstractmethod
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class PDFConverter(ABC):
    @abstractmethod
    def convert(self):
        pass


class HTMLToPDFConverter(PDFConverter):
    def __init__(self, input_file: str, output_file: str, pdf_options: dict = None):
        self.input_file = input_file
        self.output_file = output_file
        self.pdf_options = pdf_options or {}

    def convert(self):
        try:
            pdfkit.from_file(self.input_file, self.output_file, options=self.pdf_options)
            print(f"Conversion successful. PDF saved as '{self.output_file}'")
        except Exception as e:
            print(f"Conversion failed: {str(e)}")


class ConverterFactory:
    @staticmethod
    def create_converter(input_file: str, output_file: str) -> PDFConverter:
        return HTMLToPDFConverter(input_file, output_file, pdf_options={})


def parse_arguments():
    parser = argparse.ArgumentParser(description="Convert HTML to PDF using Python")
    parser.add_argument("input_file", help="Input HTML file to convert")
    parser.add_argument("output_file", help="Output PDF file name")
    return parser.parse_args()


def main():
    args = parse_arguments()

    # Create converter using factory pattern
    converter = ConverterFactory.create_converter(args.input_file, args.output_file)
    converter.convert()


if __name__ == "__main__":
    main()
