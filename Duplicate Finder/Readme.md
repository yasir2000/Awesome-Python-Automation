# Duplicate Finder Script

This script scans a given directory for duplicate files based on their MD5 hash. It provides options to delete or move the duplicate files to another directory.

## Features

- Scan a directory recursively for duplicate files.
- Filter files by minimum size.
- Display a list of duplicate files.
- Option to delete or move the duplicate files.

## Usage

1. Run the script.
2. Enter the directory you want to scan for duplicates.
3. Specify the minimum file size to consider (in bytes). By default, it's set to 0, which means all files will be considered.
4. The script will display a list of duplicate files, if any.
5. Choose an action:
   - `(D)elete`: Deletes all but one of each set of duplicate files.
   - `(M)ove`: Moves all but one of each set of duplicate files to another directory.
   - `(N)o action`: Exits the script without making any changes.

## Notes

- When choosing the delete option, the script keeps the first file it encounters and deletes the rest of the duplicates.
- When choosing the move option, the script keeps the first file it encounters and moves the rest to the specified directory. If the target directory doesn't exist, it will be created.
- The script uses MD5 hashing to identify duplicates. While MD5 is fast, it's not the most secure hashing algorithm. There's a very low probability of hash collisions (different files having the same hash), but it's something to be aware of.


## Disclaimer

Always backup your data before using scripts that modify files. The author is not responsible for any data loss.


<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->

### Explanation of Refactoring:

1. **Single Responsibility Principle (SRP)**: Each class now has a single responsibility:
   - `MD5Hashing` is responsible for calculating MD5 hashes.
   - `DuplicateFinder` is responsible for finding duplicates.
   - `ActionHandler` is responsible for deleting or moving files.

2. **Open-Closed Principle (OCP)**: Adding new hashing algorithms can be done by creating new classes that extend `HashingStrategy` without modifying existing code.

3. **Liskov Substitution Principle (LSP)**: The code adheres to LSP by ensuring any concrete strategy can be used interchangeably.

4. **Dependency Inversion Principle (DIP)**: The `DuplicateFinder` depends on the `HashingStrategy` interface, which can be injected at runtime.

5. **GoF Design Patterns**:
   - **Strategy Pattern** for the hashing algorithm.
   - **Facade Pattern** with `DuplicateFinder` to simplify the interface for finding duplicates.
   - **Chain of Responsibility** isn't directly implemented but can be adapted by extending `ActionHandler` for more actions.
