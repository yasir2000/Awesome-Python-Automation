import openpyxl
import os
from abc import ABC, abstractmethod
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class FileHandler(ABC):
    @abstractmethod
    def process_file(self, input_file: str, output_file: str, separator: str, sheet_name: str):
        pass


class CSVtoExcelConverter(FileHandler):
    def process_file(self, input_file: str, output_file: str, separator: str, sheet_name: str):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = sheet_name

        try:
            with open(input_file, "r", encoding="utf-8") as file:
                for excel_row, line in enumerate(file, start=1):
                    data = line.strip().split(separator)
                    for excel_column, value in enumerate(data, start=1):
                        sheet.cell(row=excel_row, column=excel_column, value=value)

            workbook.save(output_file)

        except FileNotFoundError:
            print("Error: The CSV file was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")


class FileProcessorFactory:
    @staticmethod
    def create_file_handler(handler_type: str) -> FileHandler:
        if handler_type == 'csv_to_excel':
            return CSVtoExcelConverter()
        raise ValueError(f"Unknown handler type: {handler_type}")


def main():
    # Get configurations from environment variables
    csv_name = os.getenv("CSV_NAME")
    sep = os.getenv("CSV_SEPARATOR")
    excel_name = os.getenv("EXCEL_NAME")
    sheet_name = os.getenv("SHEET_NAME")

    # Create file handler and process the CSV to Excel
    file_handler = FileProcessorFactory.create_file_handler('csv_to_excel')
    file_handler.process_file(csv_name, excel_name, sep, sheet_name)


if __name__ == "__main__":
    main()
