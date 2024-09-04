# Countdown Timer

This program takes in the number of seconds to countdown and displays a message when the time elapses.

# Prerequisites

It requires no prerequisites, you only need to run the script. If you don't have Python installed, you can visit [here](https://www.python.org/downloads/) to download Python.

# How to run the script

Running the script is pretty easy, open a terminal in the folder where your script is located and run the following command :

`python timer.py`

# Author's name

[KOTHA V V S AAKASH](https://github.com/AakashKotha)

<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->


### Explanation of SOLID Principles and Patterns Used

1. **Single Responsibility Principle (SRP)**: Each class has a single responsibility. The `TimeFormatter` class formats the time, while the `Timer` class handles the countdown logic.
   
2. **Open-Closed Principle (OCP)**: The design allows new types of timers or formatting styles to be added by creating new subclasses without modifying existing ones.

3. **Liskov Substitution Principle (LSP)**: Subtypes can be substituted for their base type (e.g., if `Timer` was extended, it could still work with the existing countdown method).

4. **Dependency Inversion Principle (DIP)**: The `Timer` class does not depend on a concrete implementation of time formatting but rather uses a `TimeFormatter` through composition.

5. **GoF Design Patterns**:
   - **Strategy Pattern**: The `TimeFormatter` can be considered a strategy for formatting time, allowing flexibility in formatting options.

### Environment Variables Setup

You need to create a `.env` file in the same directory as your script to define the countdown duration. Here’s an example content:

```
COUNTDOWN_DURATION=120  # Set desired countdown duration in seconds
```

### Dependencies

Make sure you have the `python-dotenv` package installed to read the environment variables. You can install it via pip:

```bash
pip install python-dotenv
```
