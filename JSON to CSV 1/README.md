## JSON TO CSV:
This script converts a JSON file to CSV file.

#### JSON :
    It means that a script (executable) file which is made of text in a programming language, is used to store and transfer the data. Python supports JSON through a built-in package called JSON

#### CSV :
    It is a simple file format used to store tabular data, such as a spreadsheet or database.
<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->

### Explanation of Design and Principles Used

1. **Single Responsibility Principle (SRP)**: Each class has a distinct responsibility:
   - `DataLoader` handles the loading of JSON data.
   - `DataWriter` is responsible for writing data to CSV.
   - `EmployeeDataProcessor` processes employee data.
   - `Application` coordinates the overall logic.

2. **Open-Closed Principle (OCP)**: Classes can be extended without modifying existing code. For example, if you want to handle XML or other formats, you can create new loader and writer classes.

3. **Liskov Substitution Principle (LSP)**: The `DataLoader` and `DataWriter` can be replaced with new implementations without affecting the `Application` logic, as long as they adhere to the expected interfaces.

4. **Inversion of Control (IoC)**: The classes depend on abstractions (like loader and writer) rather than concrete implementations.

5. **Dependency Injection**: The `Application` class accepts `DataLoader` and `DataWriter` as constructor parameters, making it easy to inject different implementations.

6. **GoF Design Patterns**:
   - **Facade Pattern**: The `Application` class acts as a facade, simplifying interaction with underlying classes.
   - **Template Method Pattern**: You could implement a template for different file loaders or writers if further variability is needed, although it wasn't explicitly shown here.

### Environment Variables

A `.env` file can be created to manage the paths of the files used in the program. Here’s an example:

```
# .env
JSON_FILE_PATH=data.json
CSV_FILE_PATH=data_file.csv
```
