# Merge Two Images

* Merges two images as required- Horizontally or Vertically.

## Usage:
* Required packages: `opencv`, Install with:
```bash
pip3 install opencv-python
```
* Run the script with:
```bash
python3 mergeImages.py
```
<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->

To refactor the provided code while adhering to SOLID principles and incorporating relevant GoF design patterns, we'll implement the following:

1. **Single Responsibility Principle (SRP)**: Separate concerns into distinct classes.
2. **Open-Closed Principle (OCP)**: Make the design extensible without modifying existing code.
3. **Liskov Substitution Principle (LSP)**: Ensure subclasses can replace their base classes without issues.
4. **Dependency Inversion Principle (DIP)**: Depend on abstractions, not concretions.
5. **Use of GoF Design Patterns**: Apply appropriate patterns as needed.


### Explanation of Changes

1. **Interface Segregation and Single Responsibility**:
   - Created `ImageMerger` as an abstract base class.
   - Separated vertical and horizontal merging into `VerticalMerger` and `HorizontalMerger`.

2. **Open-Closed Principle**:
   - New merger types can be added without modifying existing code.

3. **Liskov Substitution Principle**:
   - `VerticalMerger` and `HorizontalMerger` can be used interchangeably through `ImageProcessor`.

4. **Dependency Inversion Principle**:
   - `ImageProcessor` depends on the `ImageMerger` abstraction rather than concrete implementations.

5. **Environment Variables**:
   - Use the `dotenv` package to load environment variables (for paths, etc.), ensuring sensitive information is not hard-coded.

### .env Configuration

Create a `.env` file in the same directory with any needed variables:

```
# Example of environment variable usage
IMAGES_FOLDER=/path/to/images
```
