If a player's first two cards are an ace and a "ten-card" (a picture card or 10), giving a count of 21 in two cards, this is a natural or "blackjack." If any player has a natural and the dealer does not, the dealer immediately pays that player one and a half times the amount of their bet.
<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->

### Key Changes Made:

1. **SOLID Principles**:
    - **Single Responsibility Principle**: Each class has a clear responsibility, e.g. `Card`, `Deck`, `Player`, `Dealer`, and `GameBlackJack`.
    - **Open-Close Principle**: Classes are designed to be extended without modifying existing code (e.g., special roles can be derived from Player).
    - **Liskov Substitution Principle**: Methods and properties can be inherited from base classes without altering the expected behavior.
    - **Inversion of Control**: Card drawing logic is encapsulated in the `Deck` class, promoting separation of concerns.
    - **Dependency Injection**: Environment variables are used for betting limits rather than hard-coded values.

2. **Design Patterns**: The code structure makes use of design patterns like Factory (for card creation within the Deck class) and Strategy (for different player types could have specific strategies).

3. **Environment Variables**: Betting limits are sourced from environment variables (`MIN_BET`, `MAX_BET`) by using the `dotenv` package, improving configuration management.

4. **Readability**: Improved naming conventions and reduced complexity of the methods based on clear responsibilities.

Please ensure that you have the `python-dotenv` library installed to handle environment variables. You can install it via pip:

```bash
pip install python-dotenv
```

