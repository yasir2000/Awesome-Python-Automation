This repository consists of a list of python scripts to automate few tasks.

You can contribute by adding more python scripts which can be used to automate things. Some of already done are listed below.
Incase you have anything to be followed while executing the python script mention it as well


# Python Script

## Script  - Take a break

Python code to take a break while working long hours
TakeABreak.py


<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->

```

### Step 3: Explanation

1. **SOLID Principles**:
   - **Single Responsibility Principle**: Each class has a specific responsibility; `YouTubeBreak` only handles opening YouTube, while `BreakScheduler` manages the entire break scheduling logic.
   - **Open-Closed Principle**: New break strategies can be added without modifying existing code (e.g., you can create a `NetflixBreak` class in the future).
   - **Liskov Substitution Principle**: Any new class implementing the `BreakStrategy` can substitute the existing strategy without issues.
   - **Inversion of Control**: The break strategy is injected into the `BreakScheduler`, allowing it to function independently of the specific strategy used.
   - **Dependency Injection**: The scheduler receives its strategy via the constructor.

2. **GoF Design Patterns**:
   - **Strategy Pattern**: `BreakStrategy` interface allows for different strategies for taking breaks. This design enables dynamic selection of the break action.
   - **Facade Pattern**: The `BreakScheduler` class serves as a facade that simplifies the interaction for taking breaks.
   - **Environment Variables**: Use a `.env` file to set the number of breaks, break interval, and break URL, facilitating ease of configuration.

### Step 4: Usage of Environment Variables

Create a file named `.env` in the same directory as the script, containing:

```
TOTAL_BREAKS=3
BREAK_INTERVAL_HOURS=2
BREAK_URL=http://www.youtube.com
```
