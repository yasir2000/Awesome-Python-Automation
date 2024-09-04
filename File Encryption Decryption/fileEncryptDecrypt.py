import os
import sys
import pyAesCrypt
from dotenv import load_dotenv

load_dotenv()

# Constants loaded from ENV variables
BUFFER_SIZE = 64 * 1024  # Buffer size for encryption/decryption
PASSWORD = os.getenv("AES_PASSWORD")

class EncryptionManager:
    """Facade for file encryption and decryption operations."""

    def __init__(self, file_handler):
        self.file_handler = file_handler

    def encrypt(self, filename):
        self.file_handler.encrypt_file(filename, PASSWORD)

    def decrypt(self, filename):
        self.file_handler.decrypt_file(filename + ".aes", filename, PASSWORD)

class FileHandler:
    """Strategy for file operations based on provided algorithms."""

    def encrypt_file(self, input_file, password):
        """Encrypts a file to AES format."""
        pyAesCrypt.encryptFile(input_file, input_file + ".aes", password)
        print("File Encryption successfully done.")

    def decrypt_file(self, input_file, output_file, password):
        """Decrypts a file from AES format."""
        pyAesCrypt.decryptFile(input_file, output_file, password)
        print("File Decryption successfully done.")

def main():
    """Main function for handling command line arguments."""
    if len(sys.argv) != 2:
        print("Usage: script.py <filename>")
        return

    filename = sys.argv[1]
    file_handler = FileHandler()
    encryption_manager = EncryptionManager(file_handler)

    # Encrypt the file
    encryption_manager.encrypt(filename)

    # Decrypt the file
    encryption_manager.decrypt(filename)

if __name__ == "__main__":
    main()
