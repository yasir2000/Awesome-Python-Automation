# HTML to PDF Converter

The HTML to PDF Converter is a Python script that allows you to easily convert HTML files to PDF using the `pdfkit` library. This script provides a simple and convenient way to generate PDF documents from HTML content.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Options](#options)
- [Example](#example)
- [License](#license)

## Prerequisites

Before using this script, make sure you have the following prerequisites installed on your system:

- Python 3
- [pdfkit](https://pypi.org/project/pdfkit/) library

You can install the `pdfkit` library using pip:

```bash
pip install pdfkit

<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->

### .env File Example

Here's an example of what your `.env` file might look like:

```
PDF_OPTIONS='{"margin-top": "10", "margin-right": "10", "margin-bottom": "10", "margin-left": "10"}'
```

### Explanation of the Refactoring

1. **SOLID Principles**:
   - **Single Responsibility Principle (SRP)**: Each class has a single responsibility. `HTMLToPDFConverter` only handles conversion, while `ConverterFactory` manages object creation.
   - **Open-Closed Principle (OCP)**: The `HTMLToPDFConverter` is open for extension (you can subclass it for different formats) but closed for modification.
   - **Liskov Substitution Principle (LSP)**: `HTMLToPDFConverter` can be used wherever `PDFConverter` is expected, allowing for interchangeable use.
   - **Dependency Inversion Principle (DIP)**: High-level modules (like main) depend on abstractions (the `PDFConverter`), not concrete implementations.
   - **Inversion of Control**: The `ConverterFactory` handles the instantiation of converters rather than the main function directly creating them.

2. **GoF Design Patterns**:
   - **Factory Method**: The `ConverterFactory` class implements the factory method pattern to create converter instances without specifying exact classes.
   - **Builder Pattern (if needed)**: The `pdf_options` can be built up over time if needed, allowing customization without modification of existing classes.

3. **Environment Variables**: Configuration is managed using environment variables, enhancing flexibility and maintaining best practices for sensitive information.