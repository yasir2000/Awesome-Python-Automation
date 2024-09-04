# freelance-help-program
This software is designed to help freelancers calculate their payment based on hours worked. It takes an Excel file as input, where the start time is written in the first column and the end time is written in the second column. The software calculates the total time and the amount to be paid according to the hourly payment entered by the user.

## Installation

Layer the repository or download the code files.
Install the required dependencies by running the following command:
    pip install openpyxl
   
## Usage

1. Run the program by executing the following command:
 python calculate_payment.py

The program will open a graphical user interface (GUI) window.
Click the "Browse" button to select the Excel file containing the time values.
Enter the hourly rate in the appropriate input field.
Click the "Calculate" button to calculate the payment.
The program will display a message box with the total payment amount.
The modified Excel file with the calculated results will be saved as "modified_[original_file_name].xlsx".

Note: Make sure the Excel file has the correct format, with the start time in the first column and the end time in the second column.

<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->


### Explanation of Changes

1. **Single Responsibility Principle (SRP)**: The `FileHandler` class is responsible solely for file handling, while `PaymentCalculation` focuses solely on payment calculations. This ensures that each class has a distinct responsibility.

2. **Open/Closed Principle (OCP)**: By using the `CalculationStrategy` interface, we can easily add new calculation strategies without modifying existing code.

3. **Liskov Substitution Principle (LSP)**: `PaymentCalculation` can be replaced wherever `CalculationStrategy` is expected, ensuring interchangeable behavior.

4. **Dependency Inversion Principle (DIP)**: The `CalculatorApp` depends on the abstraction `CalculationStrategy` rather than on a concrete class, allowing for greater flexibility.

5. **GoF Design Patterns Utilized**:
   - **Strategy Pattern**: Encapsulated payment calculation logic within the `PaymentCalculation` class.
   - **Facade Pattern**: Simplified user interaction with the workbook through `FileHandler`.
   - **Template Method**: Not explicitly shown but is reflected in how `PaymentCalculation` can be structured for future extensions.

6. **Environment Variables**: Using the `dotenv` package, the application can load configurations such as file paths or settings exposed via a `.env` file.

### Sample `.env` File

Create a `.env` file in the same directory as your script, and optionally add the following:

```plaintext
# Configuration variables
EXCEL_FILE_PATH="path/to/your/file.xlsx"
PAY_PER_HOUR=20
```

