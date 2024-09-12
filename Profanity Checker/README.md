The refactored code consists of the following components:

1. **Environment Configuration**: Utilizing a `.env` file.
2. **Design Patterns**: Applying relevant GoF patterns.
3. **Class Structure**: Following SOLID principles.

Here’s the refactored code:

### .env File
```plaintext
API_URL=https://www.purgomalum.com/service/json?text=
CSV_OUTPUT_FILE=profanitycheckeroutput.csv
```

### Explanation

1. **SOLID Principles**:
   - **Single Responsibility Principle**: Each class has a single responsibility (e.g., separate classes for speech recognition, text processing, etc.).
   - **Open/Closed Principle**: The application can be easily extended with new features without modifying existing code.
   - **Liskov Substitution Principle**: Derived classes can be substituted in place of their base classes without altering the correctness.
   - **Inversion of Control**: High-level modules do not depend on low-level modules but communicate through abstractions.
   - **Dependency Injection**: Classes receive their dependencies (like API URLs) through constructor parameters or environment variables.

2. **GoF Design Patterns**:
   - **Factory Method**: Each class responsible for creating objects (like `SpeechRecognizer` or `TextProcessor`).
   - **Facade**: `Application` class simplifies interactions with various components (speech recognition, text processing, etc.).
   - **Strategy**: `SentimentAnalyzer` can easily replace or enhance sentiment analysis methods without affecting the `Application` logic.

