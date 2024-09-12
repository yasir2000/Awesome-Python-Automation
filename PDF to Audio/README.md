### .env File

Create a `.env` file in the same directory as your script with the following content:

```
PDF_FILE=python_basics.pdf
START_PAGE=1
```

### Design Principles Applied

1. **Single Responsibility Principle**: Each class has a single responsibility; `PDFReader` handles PDF operations, `TextToSpeech` manages speech output, and `PDFToSpeechFacade` orchestrates interactions.
2. **Open-Close Principle**: The code can be extended by adding new classes that adhere to existing interfaces without modifying the existing code.
3. **Liskov Substitution Principle**: Derived classes can replace the base classes without affecting the correctness of the implementation.
4. **Dependency Inversion Principle**: The higher-level `PDFToSpeechFacade` depends on abstractions (interfaces) rather than concrete implementations.
5. **Design Patterns**:
   - **Facade Pattern**: Simplifies the interaction with the `PDFReader` and `TextToSpeech`.
   - **Builder Pattern (conceptually)**: If we were to expand this example to accept parameters more dynamically, we could use a builder to configure speech settings, etc.

This refactored code maintains readability, adheres to design principles, and offers an effective way to manage configurations through environment variables. 