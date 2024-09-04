import json
import csv
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class DataLoader:
    """Class responsible for loading data from files."""
    def load_json(self, file_path: str):
        with open(file_path) as json_file:
            return json.load(json_file)

class DataWriter:
    """Class responsible for writing data to CSV files."""
    def write_csv(self, data: list, file_path: str):
        if not data:
            print("No data to write.")
            return
        
        with open(file_path, 'w', newline='') as data_file:
            csv_writer = csv.writer(data_file)
            # Writing headers based on the keys of the first dictionary
            csv_writer.writerow(data[0].keys())
            # Writing data rows
            for emp in data:
                csv_writer.writerow(emp.values())

class EmployeeDataProcessor:
    """Class responsible for processing employee data."""
    def __init__(self, data_loader: DataLoader):
        self.data_loader = data_loader

    def get_employee_data(self, file_path: str):
        data = self.data_loader.load_json(file_path)
        return data['emp_details']

class Application:
    """Main application class to coordinate loading and writing employee data."""
    def __init__(self, data_loader: DataLoader, data_writer: DataWriter):
        self.data_loader = data_loader
        self.data_writer = data_writer

    def run(self):
        json_file_path = os.getenv('JSON_FILE_PATH')
        csv_file_path = os.getenv('CSV_FILE_PATH')

        processor = EmployeeDataProcessor(self.data_loader)
        employee_data = processor.get_employee_data(json_file_path)
        
        self.data_writer.write_csv(employee_data, csv_file_path)

if __name__ == "__main__":
    data_loader = DataLoader()
    data_writer = DataWriter()
    app = Application(data_loader, data_writer)
    app.run()
