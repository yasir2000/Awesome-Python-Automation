# Password Manager

## Usage
Run the pwd_mgmr.py file and you will be prompted for the rest of the required inputs

### Getting Started:
1.  Select Option (1) Create a new key that will be used to encrypt your password file.
2.  Select Option (3) Create a new password file that will be used to hold your encrypted passwords.
3.  Select Option (5) Add a new password to the password file. \n

### Retrieving or Adding Passords:
1.  Select Option (2) Load the existing key so it can be used to encrypt new passwords or retrieve passwords from the password file.
2.  Select Option (4) Load the existing password file so it can be used to add or retrieve passwords.
3. Select Option (5) Add a new password to the password file.
4. Select Option (6) Retrieve a password for a site.

## Example

What would you like to do?
    (1) Create a new key
    (2) Load an existing key
    (3) Create new password file
    (4) Load existing password file
    (5) Add a new password
    (6) Get a password for a site
    (7) Get the list of sites
    (m) Menu
    (h) Help
    (q) Quit
Enter your choice: h
Getting Started:
    1.  Select Option (1) Create a new key that will be used to encrypt your password file.
    2.  Select Option (3) Create a new password file that will be used to hold your encrypted passwords.
    3.  Select Option (5) Add a new password to the password file.

Retrieving or Adding Passords:
    1.  Select Option (2) Load the existing key so it can be used to encrypt new passwords or retrieve passwords from the password file.
    2.  Select Option (4) Load the existing password file so it can be used to add or retrieve passwords.
    3a. Select Option (5) Add a new password to the password file.
    3b. Select Option (6) Retrieve a password for a site.
Enter your choice: 1 
Invalid Choice!
Enter your choice: 1
Enter the path: C:\pwds\mykey.key 
Enter your choice: 3
Enter the path: C:\pwds\pwds.pass
Enter your choice: 5
Enter the site: facebook
Enter the password: password123
Enter your choice: 6
What site do you want: facebook
password123
Enter your choice: 7
List of Sites:
facebook
Enter your choice: q
Bye!

<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->

To refactor the `PasswordManager` code while adhering to the SOLID principles and incorporating relevant Gang of Four (GoF) design patterns, we can break the functionality into several classes. This approach allows us to isolate responsibilities, improve maintainability, and promote flexibility. Below is a refactored version of the code:

### Changes Made
1. **Separation of Responsibilities**: 
   - **`EncryptionKeyManager`** handles key creation and loading, adhering to the **Single Responsibility Principle**.
   - **`PasswordStorage`** manages the storage and retrieval of passwords.
   - **`PasswordManagerFacade`** serves as an interface for users, simplifying interactions with the key manager and password storage.

2. **Environment Variables**: Paths for the key file and password file are now managed using environment variables, which can be set in a `.env` file. For example:
    ```
    KEY_PATH=key.key
    PASSWORD_FILE_PATH=passwords.txt
    ```

3. **Design Patterns**:
   - **Facade Pattern**: `PasswordManagerFacade` simplifies the interaction with the underlying classes.
   - **Strategy Pattern** can be further applied if encryption methods change, though not implemented here for brevity.

4. **Improved Instantiation**: All instances leverage **Dependency Injection**, allowing easy substitution or modification of components without changing the entire system.