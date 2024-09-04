# json to csv convertor

## Introduction

This Python script allows you to convert json file to csv file and save them to a specified directory. It uses json and csv library to process json files and do manupulations accordingly.

## Usage

### Prerequisites

Before using this script, ensure you have the following:

- Python installed on your system.
- Required libraries: `csv`, `json`, `python`

### Running the Script

1. Place the json file you want to convert to csv file in the same directory as this script.

2. Replace the `input_file` variable with the name of your json file name with .json extention.

```python
input_file = 'json_data.json'
python json_to_csv_with_nested_dict.py
```

### Information about  .py file

1. `json_to_csv` function
   
- This function defines the JSON to CSV converter. It takes three arguments:
- Args :
    - **json_data**: A JSON object or list of JSON objects.
    - **csv_file**: The path to the CSV file to write the data to.
    - **mapping**: A dictionary mapping JSON field names to CSV column headers.
- Returns:
    - None

1. `flatten_json` function
   
- This function flattens the JSON data. It works by recursively iterating over the JSON object and converting any nested JSON objects into a single level of key-value pairs.
  
- Args :
    - **obj**: A nested JSON object.

- Returns:
    - A flattened JSON object.

### Output

The script will create a directory named **csv_data.csv** in the same location as the script. Within this directory.

![Alt text](image.png)
<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->

### `.env`

```plaintext
INPUT_JSON_FILE=json_data.json
OUTPUT_CSV_FILE=csv_data.csv
```

### Explanation

1. **Single Responsibility Principle**: Each class has a single responsibility: `JSONFlattener` handles flattening, while `JSONToCSVConverter` deals with the conversion process. The configuration is centralized in the `Config` class.

2. **Open-Closed Principle**: You can extend the functionality (e.g., adding more mappings or flattening logic) without modifying existing code.

3. **Liskov Substitution Principle**: Subclasses can replace the original classes without altering the program's correctness, as they all follow the same interface for processing.

4. **Inversion of Control & Dependency Injection**: Dependencies are injected into the constructor of `JSONToCSVConverter`, making it flexible and easily testable.

5. **Design Patterns**:
   - **Facade Pattern**: The `JSONToCSVConverter` provides a simple method to convert JSON to CSV without exposing details of the process.
   - **Template Method Pattern**: In this example, we could abstract the method of flattening depending on the class, maintaining a skeleton while allowing subclasses to specify behavior.

