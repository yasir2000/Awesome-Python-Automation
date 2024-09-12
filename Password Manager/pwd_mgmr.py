from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class EncryptionKeyManager:
    """Handles encryption key creation and loading."""
    
    def __init__(self, path):
        self.path = path
        self.key = None

    def create_key(self):
        self.key = Fernet.generate_key()
        with open(self.path, 'wb') as f:
            f.write(self.key)

    def load_key(self):
        with open(self.path, 'rb') as f:
            self.key = f.read()
        return self.key


class PasswordStorage:
    """Handles loading and storing passwords."""
    
    def __init__(self, key_manager):
        self.key_manager = key_manager
        self.pwd_dict = {}

    def load_pwd_file(self, path):
        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.pwd_dict[site] = self.decrypt_password(encrypted)

    def add_password(self, site, password, path):
        self.pwd_dict[site] = password
        encrypted = self.encrypt_password(password)
        with open(path, 'a') as f:
            f.write(f"{site}:{encrypted.decode()}\n")

    def encrypt_password(self, password):
        return Fernet(self.key_manager.key).encrypt(password.encode())

    def decrypt_password(self, encrypted):
        return Fernet(self.key_manager.key).decrypt(encrypted.encode()).decode()

    def get_password(self, site):
        return self.pwd_dict.get(site, "Password not found.")

    def get_sites(self):
        return list(self.pwd_dict.keys())


class PasswordManagerFacade:
    """Facade for simplifying the interaction with the password manager."""
    
    def __init__(self, key_manager: EncryptionKeyManager, storage: PasswordStorage):
        self.key_manager = key_manager
        self.storage = storage

    def create_key(self):
        self.key_manager.create_key()

    def load_key(self):
        return self.key_manager.load_key()

    def load_password_file(self, path):
        self.storage.load_pwd_file(path)

    def add_password(self, site, password, path):
        self.storage.add_password(site, password, path)

    def get_password(self, site):
        return self.storage.get_password(site)

    def get_sites(self):
        return self.storage.get_sites()


def main():
    # Environment variables for file paths
    key_path = os.getenv('KEY_PATH', 'key.key')
    password_file_path = os.getenv('PASSWORD_FILE_PATH', 'passwords.txt')

    key_manager = EncryptionKeyManager(key_path)
    storage = PasswordStorage(key_manager)
    pm_facade = PasswordManagerFacade(key_manager, storage)

    print("What would you like to do?")
    done = False

