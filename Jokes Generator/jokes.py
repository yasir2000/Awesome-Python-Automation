import os
from dotenv import load_dotenv
import pyjokes

# Load environment variables
load_dotenv()

# Define interfaces for Joke Providers and Languages
class JokeProvider:
    def get_joke(self, category: str, language: str) -> str:
        pass

class LanguageProvider:
    def get_language(self, op: int) -> str:
        pass

# Concrete implementation of JokeProvider
class PyJokesProvider(JokeProvider):
    def get_joke(self, category: str, language: str) -> str:
        return pyjokes.get_joke(language=language, category=category)

# Concrete implementation of LanguageProvider
class SimpleLanguageProvider(LanguageProvider):
    def get_language(self, op: int) -> str:
        if op == 3:
            return "de"
        return "en" if op in [1, 2, 4] else "en"

# Strategy pattern for selecting categories
class JokeCategory:
    @staticmethod
    def get_category(op: int) -> str:
        categories = {1: "neutral", 2: "chuck", 3: "twister", 4: "all"}
        return categories.get(op, "neutral")

# Facade for Joke Service
class JokeService:
    def __init__(self, joke_provider: JokeProvider, language_provider: LanguageProvider):
        self.joke_provider = joke_provider
        self.language_provider = language_provider

    def fetch_joke(self, option: int) -> str:
        category = JokeCategory.get_category(option)
        language = self.language_provider.get_language(option)
        return self.joke_provider.get_joke(category, language)

# Main program with dependency injection
class JokeApp:
    def __init__(self):
        self.joke_service = JokeService(PyJokesProvider(), SimpleLanguageProvider())
        self.option = 0

    def run(self):
        print("MENU\n1. Neutral\n2. Chuck Norris jokes\n3. Twisters(in German)\n4. All\n5. Exit.")
        while self.option != 5:
            try:
                self.option = int(input("Enter option: "))
                if self.option == 5:
                    print("Successfully exited!")
                    break
                joke = self.joke_service.fetch_joke(self.option)
                print(joke)
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    app = JokeApp()
    app.run()
