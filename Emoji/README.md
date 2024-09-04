### Explanation:

1. **SOLID Principles**:
   - **Single Responsibility Principle**: Each class has a single responsibility: `Config` manages environment variables; `PDFFactory` creates a PDF canvas; `PDFBuilder` performs operations related to the PDF creation; `CreatePDFCommand` encapsulates the creation logic.
   - **Open/Close Principle**: The system can be extended with new output formats or content types without modifying existing code.
   - **Liskov Substitution Principle**: Classes implementing interfaces or extending base classes can replace their parent classes without affecting functionality.
   - **Inversion of Control**: High-level modules (`CreatePDFCommand`) depend on abstractions (`PDFBuilder`) rather than concrete implementations.
   - **Dependency Injection**: `PDFBuilder` is injected with a `PDFFactory` instance, enabling flexible canvas creation.

2. **GoF Design Patterns**:
   - **Abstract Factory**: Used for creating a canvas without specifying the details of its creation.
   - **Builder**: Constructs the PDF by separating the steps of registration, content addition, and saving.
   - **Command**: Encapsulates all actions required to create the PDF into a single command object.

3. **Environment Variables**: 
   - Configurable using `.env` files or environment variables to manage outputs and configurations.

### .env Configuration

You should create a `.env` file in the same directory as your script with the following content:

```
PDF_OUTPUT_FILENAME=emoji.pdf
PDF_EMOJI=😊
PDF_FONT_PATH=emoji.tiff
```

