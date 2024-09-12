import random
import string
import os
from dotenv import load_dotenv

load_dotenv()

# Constants
CHARACTERS = ['@', '#', '$', '%', '&', '?']


class PasswordConfig:
    """Configuration class to manage password settings."""
    def __init__(self, length):
        self.length = length
        self.alphabet_count = random.randint(2, length - 1)
        self.number_count = random.randint(1, length - self.alphabet_count - 1)
        self.symbol_count = length - (self.alphabet_count + self.number_count)


class PasswordBuilder:
    """Builder for constructing Password with various components."""
    def __init__(self, config):
        self.config = config
        self.password_parts = []

    def add_uppercase_letters(self):
        uppercases = random.choices(string.ascii_uppercase, k=random.randint(0, self.config.alphabet_count))
        self.password_parts.extend(uppercases)

    def add_lowercase_letters(self):
        lowercases = random.choices(string.ascii_lowercase, k=self.config.alphabet_count - len(self.password_parts))
        self.password_parts.extend(lowercases)

    def add_numbers(self):
        numbers = random.choices(string.digits, k=self.config.number_count)
        self.password_parts.extend(numbers)

    def add_symbols(self):
        symbols = random.choices(CHARACTERS, k=self.config.symbol_count)
        self.password_parts.extend(symbols)

    def build(self):
        random.shuffle(self.password_parts)
        return ''.join(self.password_parts)


class PasswordGenerator:
    """Facade for generating a password."""
    def __init__(self, config):
        self.config = config

    def generate_password(self):
        builder = PasswordBuilder(self.config)
        builder.add_uppercase_letters()
        builder.add_lowercase_letters()
        builder.add_numbers()
        builder.add_symbols()
        return builder.build()


if __name__ == '__main__':
    # Load password length from .env
    password_length = int(os.getenv('PASSWORD_LENGTH', 12))
    config = PasswordConfig(length=password_length)
    
    generator = PasswordGenerator(config)
    password = generator.generate_password()
    
    print(f"Generated Password: {password}\n")
