# Arrange It

With the help of this script, files can be moved automatically to the folder that corresponds to their extension (for example, ".jpg" or ".png" ==> "/Pictures," and ".mp4" ==> "/Videos").

## How To Run

- Put in Download Folder Or Wherever You want to automatically move the file and Just run

For CLI

Explanation of Refactoring:
Single Responsibility Principle (SRP):

DirectoryManager manages directory creation and structure.
FileOrganizer manages the organization of files based on their types.
Open/Closed Principle (OCP):

Classes can be extended (e.g., adding new file types) without modifying existing code.
Liskov Substitution Principle (LSP):

Classes can be extended or replaced without affecting the program behavior.
Dependency Inversion Principle (DIP):

FileOrganizer depends on DirectoryManager abstraction.
Use of .env for Configuration:

The directory structure is loaded from a .env file, making it configurable without code changes.
Organizational Patterns:

Created a clear separation of tasks, resembling the Strategy Pattern (different file types) and Facade Pattern (simplifying user interaction with folder and file organization).

```bash
python arrangeit.py

<!-- This is a manual change to ensure the file is tracked and updated -->
```

<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->