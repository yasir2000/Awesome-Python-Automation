import os
import json
import csv
from dotenv import load_dotenv
from .json_flattener import JSONFlattener

class JSONToCSVConverter:
    def __init__(self, input_file, output_file, mapping=None):
        self.input_file = input_file
        self.output_file = output_file
        self.mapping = mapping or {}

    def convert(self):
        with open(self.input_file, 'r', encoding='utf-8-sig') as json_file:
            json_data = json.load(json_file)

        flattener = JSONFlattener()
        if isinstance(json_data, list):
            json_data = [flattener.flatten(obj) for obj in json_data]

        column_headers = self.mapping or json_data[0].keys()

        with open(self.output_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(column_headers)

            for row in json_data:
                row_values = [str(row.get(column, "")) for column in column_headers]
                writer.writerow(row_values)

