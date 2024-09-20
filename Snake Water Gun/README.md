### Explanation of the Design Patterns and SOLID Principles Used

1. **Single Responsibility Principle (SRP)**:
   - Each class has distinct responsibilities:
     - `GameStrategy`: Defines a strategy for the game.
     - `SnakeWaterGunStrategy`: Implements the strategy for the Rock-Paper-Scissors game.
     - `Game`: Manages the game logic and user interaction.

2. **Open/Closed Principle (OCP)**:
   - New game strategies can be added by extending `GameStrategy` without modifying the existing game logic.

3. **Liskov Substitution Principle (LSP)**:
   - You can replace `SnakeWaterGunStrategy` with any other strategy conforming to the `GameStrategy` interface without affecting the game execution.

4. **Dependency Inversion Principle (DIP)**:
   - The `Game` class depends on the abstraction `GameStrategy`, promoting flexibility and reducing dependency on concrete implementations.

5. **Design Patterns**:
   - **Strategy Pattern**: Encapsulates the gameplay algorithm into a strategy interface and allows swapping of algorithms.
   - **Factory Method**: Implicitly used in the selection of strategies, where different strategies could be instantiated easily.

### Environment Variable Setup

Here’s a sample `.env` file:

```
ROUNDS=3
```

