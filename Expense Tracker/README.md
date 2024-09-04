## Expense tracker

### Usage

Install the required dependencies using pip:

```
pip install -r requirements.txt
```

Run the expense.py file to start the bot:

```
python expense.py
```

<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->

### Breakdown of the Refactor
1. **Environment Configuration**: We're using `dotenv` to load the CSV file path from an environment variable.
2. **Singleton Pattern**: `ExpenseManager` is implemented as a singleton to ensure a single instance is managing all expenses.
3. **Factory Method**: An abstraction layer in the form of `ExpenseView` that manages how expenses are displayed.
4. **Separation of Concerns**: Each class has a distinct responsibility, adhering to the Single-Responsibility Principle and other SOLID principles.

### Advantages of Refactoring
- **Scalability**: New features can easily be added without modifying existing classes.
- **Maintainability**: Each class serves a specific role, making it easier to manage and understand.
- **Reusability**: Components can be reused in different contexts (e.g., adding new types of expense views).

