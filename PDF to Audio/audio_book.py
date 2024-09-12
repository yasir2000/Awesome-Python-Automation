import os
import pyttsx3
import PyPDF2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class PDFReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.pdf_reader = None

    def open_pdf(self):
        book = open(self.file_path, 'rb')
        self.pdf_reader = PyPDF2.PdfReader(book)

    def get_page_count(self):
        return len(self.pdf_reader.pages)

    def get_page_text(self, page_number):
        page = self.pdf_reader.pages[page_number]
        return page.extract_text()

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

class PDFToSpeechFacade:
    def __init__(self, pdf_reader: PDFReader, tts: TextToSpeech):
        self.pdf_reader = pdf_reader
        self.tts = tts

    def read_pdf(self, start_page):
        self.pdf_reader.open_pdf()
        page_count = self.pdf_reader.get_page_count()

        for num in range(start_page, page_count):
            text = self.pdf_reader.get_page_text(num)
            if text:
                self.tts.speak(text)

def main():
    # Retrieve from environment variables
    pdf_file = os.getenv('PDF_FILE', 'python_basics.pdf')
    start_page_user_input = os.getenv('START_PAGE', '1')
    
    try:
        start_page = int(start_page_user_input) - 1
    except ValueError:
        print("Invalid page number. Please provide a valid integer.")
        return

    # Initialize components
    pdf_reader = PDFReader(pdf_file)
    tts = TextToSpeech()
    pdf_facade = PDFToSpeechFacade(pdf_reader, tts)

    # Read the PDF starting from the specified page
    pdf_facade.read_pdf(start_page)

if __name__ == "__main__":
    main()
