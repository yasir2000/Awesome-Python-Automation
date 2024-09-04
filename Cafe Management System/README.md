# Cafe Management System

- This is a cafe Management System Coded by Python using `tkinter` library.
- You need to install `Pillow`by entering `pip install Pillow`.
<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->

### Key Changes Explained:

1. **Single Responsibility Principle**: Each class (`PriceList`, `Order`, `CafeManagementApp`) now has a single responsibility. `PriceList` handles pricing, `Order` computes the total from item quantities, and `CafeManagementApp` manages the UI.

2. **Open/Closed Principle**: The design allows for easy modification or extension (e.g., adding more items to the menu) without altering existing code.

3. **Liskov Substitution Principle**: Item quantities can be substituted or replaced without affecting the functionality.

4. **Interface Segregation Principle**: In this case, methods are divided based on functionality, maintaining clear responsibilities.

5. **Dependency Inversion Principle**: Higher-level modules (`PriceList`, `Order`) are not dependent on lower-level modules but interact through defined interfaces.

6. **Usage of Design Patterns**:
   - **Strategy Pattern**: The `Order` class can be extended to apply discounts or change calculation strategies without modifying its structure.
   - **Factory Method**: You could create a factory to instantiate different `Order` types if needed.

