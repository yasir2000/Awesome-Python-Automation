Image-Manipulation-using-Python-without-external-libraries
---
Image manipulation techniques in Python without using external libraries like OpenCV, Pillow, etc

Includes the following manipulations:

- Channel-wise Addition
- Invert Colors
- Mirror Vertical
- Mirror Horizontal
- Blur(2 methods)
- Resize
- Lightness
- Brightness
- Contrast

<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->


### Explanation of Refactoring

1. **Single Responsibility Principle (SRP)**: Each class now has one clear responsibility. For example, `Inverter` only handles image inversion, while `Blur` focuses solely on blurring.

2. **Open/Closed Principle (OCP)**: The code is designed to be open for extension through the `ImageProcessorFactory`, allowing new types of processors to be added without modifying existing code.

3. **Liskov Substitution Principle (LSP)**: All `ImageProcessor` subclasses can replace their parent class type without breaking the code. The `ImageContext` uses the processors interchangeably.

4. **Dependency Inversion Principle (DIP)**: High-level modules (`ImageContext`) do not depend on low-level modules but depend on abstractions (the `ImageProcessor` interface).

5. **GoF Design Patterns**:
   - **Factory Method**: The `ImageProcessorFactory` simplifies object creation based on type.
   - **Strategy Pattern**: The `ImageContext` uses various `ImageProcessor` implementations dynamically.
   - **Adapter Pattern (conceptual)**: Each processor adheres to the same interface, allowing the context to manipulate them uniformly.

