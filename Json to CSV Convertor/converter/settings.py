import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    INPUT_JSON_FILE = os.getenv("INPUT_JSON_FILE", "default_input.json")
    OUTPUT_CSV_FILE = os.getenv("OUTPUT_CSV_FILE", "default_output.csv")
    MAPPING = {
        "name": "Name",
        "status": "Status",
        "date": "Date",
        "author": "Author",
        "probability": "Probability",
        "result": "Result",
        "final_status": "Final Status",
        "connected.run_again": "Run Again",
        "connected.next_test": "Next Test",
        "connected.next_test_status": "Next Test Status",
    }
