### Directory Structure
```
project/
│
├── .env
├── main.py
└── ascii_image/
    └── ascii_image.txt
```

### .env file
```plaintext
NEW_WIDTH=100
OUTPUT_PATH=ascii_image/ascii_image.txt
ASCII_CHARS="@#S%?*+;:,."
```


### Explanation of Refactoring

1. **Single Responsibility Principle (SRP):**
   - The `AsciiArtGenerator` class handles all functionalities related to image processing. The `AsciiArtApp` class manages user interactions.

2. **Open/Closed Principle (OCP):**
   - The architecture allows for easy extension without modifying existing code. If you want to add different image processing strategies or adjust the ASCII characters, you can do so without changing the core logic of the existing classes.

3. **Liskov Substitution Principle (LSP):**
   - You can replace image processing strategies or add new types of resizing and character mapping without affecting the functionality. For instance, you could extend `AsciiArtGenerator` with new methods that override behavior for specific images or conditions.

4. **Dependency Inversion Principle (DIP):**
   - `AsciiArtApp` depends on the abstraction of `AsciiArtGenerator`, allowing for easy swapping of the generator without having to change the app's logic.

5. **Design Patterns:**
   - **Factory Method:** While not explicitly written out, you could further enhance this code with factories to create different `AsciiArtGenerator` instances based on application needs.
   - **Strategy Pattern:** The generation logic could be varied by creating subclasses of `AsciiArtGenerator` that handle different algorithms for converting images to ASCII.
   - **Facade Pattern:** The `AsciiArtApp` acts as a facade, providing a simple interface for a user to interact with parts of the image processing functionality.

