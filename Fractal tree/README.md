# Fractal trees in python

<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->


### .env File

Create a `.env` file in the same directory as your script with the following content:

```
BRANCH_LENGTH=250
```

### Explanation of Refactoring

1. **SOLID Principles**:
   - **Single Responsibility Principle**: Each class has a single responsibility. `TurtleFacade` manages the turtle setup and exposes tree drawing functionality, while `TreeBuilder` handles the recursive tree drawing logic.
   - **Open/Closed Principle**: The classes can be extended for new turtle behaviors without modifying existing code.
   - **Liskov Substitution Principle**: Objects of the `TurtleAdapter` can be replaced with any other adapter implementing the expected methods without affecting the `TreeBuilder` logic.
   - **Dependency Inversion**: The `TreeBuilder` depends on an abstraction (`TurtleAdapter`) rather than concrete details.
   - **Dependency Injection**: `TurtleAdapter` is injected into `TreeBuilder`, allowing for more flexible testing and implementation.

2. **GoF Design Patterns**:
   - **Facade**: `TurtleFacade` simplifies the interface for turtle drawing operations.
   - **Adapter**: `TurtleAdapter` wraps the turtle class, allowing for a simpler interface that accommodates future modifications.
   - **Builder**: `TreeBuilder` separates the tree construction logic, making it modular.

This refactoring enhances code maintainability, readability, and configurability through the use of `.env` variables. Each change point adheres to both the SOLID principles and relevant design patterns, ensuring your turtle graphics project is structured and scalable. 