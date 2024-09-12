#QR Ticket Generator from Excel File

This project is a QR ticket generator that converts data from an Excel file into QR codes for ticket generation.


###Features


1. Read data from an Excel file.

2. Generate QR codes based on the data.

3. Save QR codes as image files.

4. Print tickets with QR codes.

###Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.


<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->

### Refactoring Plan

1. **Single Responsibility Principle**: Each class or function should have only one reason to change.
   - Separate responsibilities into distinct classes:
     - **QR Code Generation**: A dedicated class for handling QR code functionality.
     - **PDF Generation**: A dedicated class for creating PDFs.
     - **Email Sending**: A dedicated class for managing email functionality.
     - **Data Management**: A class for handling data (reading from Excel, etc.).
     
2. **Open/Closed Principle**: Software entities should be open for extension but closed for modification.
   - Implement interfaces for QR code generation and PDF generation, allowing new methods to be added without changing existing code.
   
3. **Liskov Substitution Principle**: Subtypes must be substitutable for their base types.
   - Ensure that any derived class of a base class can be used without affecting the correctness of the program.

4. **Interface Segregation Principle**: Clients should not be forced to depend on interfaces they do not use.
   - Break down large interfaces into smaller, more specific ones.

5. **Dependency Inversion Principle**: Depend on abstractions, not on concretions. 
   - Use dependency injection to allow for easier testing and swapping of implementations.

### Design Patterns to Implement

1. **Factory Method**: Create a factory class to generate QR codes and PDFs based on provided parameters.
2. **Observer**: Implement an observer pattern to notify the system (or the user) when a QR code or PDF is generated.
3. **Strategy**: Utilize strategy for email sending logic to allow different email providers to be integrated easily.
4. **Facade**: Provide a façade class that simplifies the interface to the whole system, making it easier to use without exposing its complexities.
