
### .env File
```plaintext
# .env file
PASSWORD_LENGTH=12
```


### Explanation of Refactoring
1. **Classes and Responsibilities**:
    - **PasswordConfig**: Responsible for holding the configuration related to password lengths and counts.
    - **PasswordBuilder**: Implements various methods to add different character types to the password based on the configuration.
    - **PasswordGenerator**: Acts as a facade that provides a simple interface to generate a password by delegating tasks to the builder.

2. **SOLID Principles**:
    - **Single Responsibility Principle**: Each class has a single responsibility.
    - **Open/Closed Principle**: The design allows for the easy addition of new character types or configurations without modifying existing code.
    - **Liskov Substitution Principle**: All character types can be independently modified without causing issues elsewhere.
    - **Inversion of Control and Dependency Injection**: The password generator takes a configuration object, separating the responsibility of passing in configuration from the building of the password.

3. **GoF Design Patterns**:
    - **Builder Pattern**: Used in `PasswordBuilder` to separate construction processes of different password components.
    - **Facade Pattern**: `PasswordGenerator` wraps the complexity of password generation, offering a simple interface.
  