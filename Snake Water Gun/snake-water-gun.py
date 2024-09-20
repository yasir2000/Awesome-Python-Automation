import random
import os
from abc import ABC, abstractmethod
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants from environment variables
ROUNDS = int(os.getenv('ROUNDS', 3))

# Strategy Pattern: Define the strategy interface
class GameStrategy(ABC):
    @abstractmethod
    def play(self, user_choice: str) -> str:
        pass

# Concrete strategies
class SnakeWaterGunStrategy(GameStrategy):
    choices = ['Snake', 'Water', 'Gun']

    def play(self, user_choice: str) -> str:
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(user_choice, computer_choice)
        return computer_choice, result

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'tie'
        win_conditions = {
            'Snake': 'Water',
            'Water': 'Gun',
            'Gun': 'Snake'
        }
        return 'computer wins' if win_conditions[user_choice] == computer_choice else 'user wins'

# Game class for managing the game flow
class Game:
    def __init__(self, rounds: int, strategy: GameStrategy):
        self.rounds = rounds
        self.strategy = strategy
        self.user_score = 0
        self.computer_score = 0

    def get_user_choice(self):
        choice_map = {1: 'Snake', 2: 'Water', 3: 'Gun'}
        print("Enter a number for your choice:")
        for num, choice in choice_map.items():
            print(f"{num}. {choice}")
        while True:
            try:
                user_input = int(input())
                if user_input in choice_map:
                    return choice_map[user_input]
                else:
                    print("Invalid choice, please try again.")
            except ValueError:
                print("Please enter a number.")

    def play(self):
        for turn in range(self.rounds):
            user_choice = self.get_user_choice()
            computer_choice, result = self.strategy.play(user_choice)
            print(f"Computer's choice: {computer_choice}")
            print(f"Result: {result}")

            if result == 'user wins':
                self.user_score += 1
            elif result == 'computer wins':
                self.computer_score += 1

        self.display_final_score()

    def display_final_score(self):
        print(f"Game over! User: {self.user_score}, Computer: {self.computer_score}")

# Entry point to start the game
if __name__ == "__main__":
    strategy = SnakeWaterGunStrategy()
    game = Game(ROUNDS, strategy)
    game.play()
