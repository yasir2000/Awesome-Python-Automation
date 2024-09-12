import os
from cryptography.fernet import Fernet

class KeyGenerator:
    """Responsible for generating and saving a key."""
    
    @staticmethod
    def generate_key():
        """Generate a new Fernet key."""
        key = Fernet.generate_key()
        with open('encryption_key.txt', 'wb') as file:
            file.write(key)
        return key

def main():
    KeyGenerator.generate_key()

if __name__ == '__main__':
    main()
