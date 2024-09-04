This repository consists of a list of python scripts to automate few tasks.

You can contribute by adding more python scripts which can be used to automate things. Some of already done are listed below.
Incase you have anything to be followed while executing the python script mention it as well


# Python Script


## Script - File Encryption Decryption

Developed File Encryption Decryption Simple Algorithm using python pyAedCrypt module
Files can be encrypted using desired password.
fileEncryptDecrypt.py



<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->

### Design Principles and Patterns Applied
1. **Single Responsibility Principle (SRP)**: 
   - Each class (`EncryptionManager` and `FileHandler`) has a single responsibility (managing encryption/decryption logic and file handling, respectively).
  
2. **Open/Closed Principle (OCP)**: 
   - The `FileHandler` class can be easily modified to support different encryption libraries while leaving the `EncryptionManager` interface unchanged.

3. **Liskov Substitution Principle (LSP)**: 
   - Classes can be extended for different file handling or encryption methods without altering the functionality of existing code.

4. **Inversion of Control (IoC)**: 
   - The `EncryptionManager` is decoupled from the `FileHandler` class implementation through dependency injection.

5. **Dependency Injection**: 
   - `EncryptionManager` receives an instance of `FileHandler`, allowing for easier testing and modification.

### Design Patterns Applied
- **Facade**: `EncryptionManager` simplifies the encryption/decryption process by providing a unified interface.
- **Strategy**: `FileHandler` enables the choice of file operation strategy, making it easy to swap in new encryption methods or libraries.
- **Template Method**: Though not fully illustrated, this pattern can be easily expanded by adding abstract base classes for different encryption methods.

