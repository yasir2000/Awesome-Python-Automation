This repository consists of a list of python scripts to automate few tasks.

You can contribute by adding more python scripts which can be used to automate things. Some of already done are listed below.
Incase you have anything to be followed while executing the python script mention it as well


# Python Script

## Script  - Digital Clock

DigitalClock.py

<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->

To refactor the given code following the SOLID principles and applying relevant Gang of Four (GoF) design patterns, we'll architect the digital clock application in a more modular way. The refactored code will utilize Dependency Injection for better testability, employ single responsibility for each class, and ensure that it can be easily extended or modified.


### Explanation of Refactor Using Design Principles and Patterns

1. **Single Responsibility Principle**: Each class has a specific responsibility:
    - `TimeProvider` handles fetching the current time.
    - `ClockLabel` is responsible for creating and updating the label in the GUI.
    - `DigitalClockApp` manages the overall application structure and flow.

2. **Open/Closed Principle**: New features can be added, such as different time formats or themes, by creating new classes without modifying existing ones.

3. **Liskov Substitution Principle**: Each class can be substituted with any subclass without altering the correctness of the program. For instance, if we create a different `TimeProvider` that fetches time from an API, the `ClockLabel` will work without change.

4. **Inversion of Control**: The `DigitalClockApp` composes its dependencies, like `ClockLabel`, making it easy to modify or replace components as needed.

5. **Dependency Injection**: The `ClockLabel` class does not instantiate its own label but receives a parent from the `DigitalClockApp`.

### Utilization of GoF Design Patterns

- **Facade Pattern**: The `DigitalClockApp` acts as a facade to set up the entire clock functionality.
- **Strategy Pattern**: If time representation is changed (e.g., 12-hour to 24-hour), it can be switched easily by modifying the `TimeProvider` methods.
- **Decorator Pattern**: Future extensions, such as adding more UI features or decorations, can be done without changing the existing `ClockLabel`.

### Environment Variables Example

Create a `.env` file in the same directory as your script with the following content:

```
CLOCK_BACKGROUND=red
CLOCK_FOREGROUND=black
```

### Steps to Run the Application

1. Make sure you have the `python-dotenv` module installed. You can install it using:
   ```bash
   pip install python-dotenv
   ```
   
2. Place the provided code in a Python file, e.g., `digital_clock.py`.

3. Create a `.env` file with the specified contents.

4. Run the application:
   ```bash
   python digital_clock.py
   ```

This refactored code embodies the principles and patterns discussed, making it cleaner, more maintainable, and easier to extend. 