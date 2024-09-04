from converter.json_to_csv_converter import JSONToCSVConverter
from converter.settings import Config

def main():
    converter = JSONToCSVConverter(Config.INPUT_JSON_FILE, Config.OUTPUT_CSV_FILE, Config.MAPPING)
    converter.convert()
    print(f"Conversion from JSON to CSV completed successfully. CSV file saved as {Config.OUTPUT_CSV_FILE}")

if __name__ == "__main__":
    main()
