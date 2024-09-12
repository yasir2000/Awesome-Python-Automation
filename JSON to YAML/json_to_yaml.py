import os
import sys
import json
import yaml
from abc import ABC, abstractmethod

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Environment variable defaults
SOURCE_FILE_ENV = os.getenv("SOURCE_FILE", "source.json")
TARGET_FILE_ENV = os.getenv("TARGET_FILE", "output.yaml")

# Command interface (Command Pattern)
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# JSON to YAML conversion (Strategy Pattern)
class JsonToYamlConverter:
    def convert(self, json_data):
        return yaml.dump(json_data)

# File handler (Facade Pattern)
class FileHandler:
    def read(self, filepath):
        with open(filepath, 'r') as file:
            return json.load(file)

    def write(self, filepath, data):
        with open(filepath, 'w') as file:
            file.write(data)

# Application entry point
class JsonYamlApp:
    def __init__(self, source_file, target_file):
        self.source_file = source_file
        self.target_file = target_file
        self.file_handler = FileHandler()
        self.converter = JsonToYamlConverter()

    def run(self):
        try:
            json_data = self.file_handler.read(self.source_file)
            yaml_data = self.converter.convert(json_data)

            if self.target_file:
                self.file_handler.write(self.target_file, yaml_data)
            else:
                print(yaml_data)
        except FileNotFoundError as e:
            print(f"ERROR: {e}")
            exit(1)

# Dependency Injection / Inversion of Control
if __name__ == "__main__":
    source_file = sys.argv[1] if len(sys.argv) > 1 else SOURCE_FILE_ENV
    target_file = sys.argv[2] if len(sys.argv) > 2 else None
    app = JsonYamlApp(source_file, target_file)
    app.run()
