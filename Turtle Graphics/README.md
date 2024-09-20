This repository consists of a list of python scripts to automate few tasks.

You can contribute by adding more python scripts which can be used to automate things. Some of already done are listed below.
Incase you have anything to be followed while executing the python script mention it as well


# Python Script

## Script  - Turtle Graphics

Code using turtle graphics
TurtleGraphics.py


<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->

1. **Single Responsibility Principle (SRP)**: Each class should have only one reason to change.
2. **Open Closed Principle (OCP)**: Classes should be open for extension but closed for modification.
3. **Liskov Substitution Principle (LSP)**: Subclasses should be substitutable for their base classes.
4. **Dependency Inversion Principle (DIP)**: Depend on abstractions, not on concrete implementations.
5. **Interface Segregation Principle (ISP)**: Many client-specific interfaces are better than one general-purpose interface.

We will also use the following design patterns:
- **Factory Method**: To create the turtle.
- **Builder**: To construct and configure the turtle.
- **Singleton**: To ensure only one instance of the screen.
- **Strategy**: To handle different draw strategies.
- **Adapter**: For environment variables.

### 1. Environment File `.env`
```env
BACKGROUND_COLOR=pink
TURTLE_SHAPE=turtle
TURTLE_COLOR=green
TURTLE_SPEED=5
FORWARD_DISTANCE=100
TURN_ANGLE=90
ROTATE_ANGLE=10
FINAL_MOVE_DISTANCE=300
NUM_SQUARES=37
```

### Explanation:

1. **Environment Variables**: Stored configuration in a `.env` file and loaded it using `dotenv`.
2. **Singleton**: Implemented for the `TurtleScreen` class to ensure only one screen instance.
3. **Factory Method**: Created a factory for the turtle.
4. **Builder Pattern**: Built and configured the turtle in a step-by-step manner.
5. **Strategy Pattern**: Used to define different drawing strategies.
6. **Adapter**: Environment variables are accessed using an adapter class (`Config`).
7. **SOLID Principles**: Followed throughout the refactoring process to ensure extensibility, maintainability, and ease of understanding.

This refactored code adheres to the SOLID principles and GoF design patterns while using environment variables efficiently. 