# JOKES GENERATOR
### Generates jokes of different categories such as netural , chuck norris ,tongue twisters...

This python code takes user input of different category of jokes and gives out jokes based on the user prefered category.

#### Requirements:
* Install pyjokes module
* run `pip install pyjokes`

### Usage
* Clone the repo 
* open the `Jokes-generator` folder
##### for windows
* run `python jokes.py`
##### for linux
* run `python3 jokes.py`

<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->

### Explanation of Design and Principles Used

1. **Single Responsibility Principle (SRP)**: Each class has a single responsibility. For instance, `JokeProvider` handles joke retrieval, while `LanguageProvider` handles language determination.

2. **Open-Closed Principle (OCP)**: The `JokeProvider` and `LanguageProvider` can be extended without modifying existing code. New categories or joke providers can be added easily.

3. **Liskov Substitution Principle (LSP)**: The `JokeProvider` and `LanguageProvider` interfaces allow any implementation to be used interchangeably without altering functionality.

4. **Dependency Inversion Principle (DIP)**: The `JokeService` depends on abstractions `JokeProvider` and `LanguageProvider`, allowing for easy swapping of implementations.

5. **GoF Design Patterns**:
   - **Facade Pattern**: `JokeService` serves as a facade to simplify interaction with multiple classes involved in joke retrieval.
   - **Strategy Pattern**: The `JokeCategory` class encapsulates the logic of selecting a joke category based on the user input.

### Environment Variables

A `.env` file can be created to manage sensitive variables or configurations. Here’s an example:

```
# .env
# Configuration for Joke app
JOKE_PROVIDER=pyjokes
LANGUAGE_PROVIDER=simple
```

