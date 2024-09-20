# Text-to-Image

## Usage
Run the text2image.py file from the directory where the Python-Scripts folder is located in and it will prompt you will all the required inputs

### Example
```bash
cd code
python3 code/Python-Scripts/Text-To-Image/text2image.py
```

## Output
The saved JPEG file will be located in the directory
<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->

### Explanation of Refactor

1. **SOLID Principles**:
   - **Single Responsibility Principle**: Each class has a single responsibility; `ImageConfig` handles configurations, while `ImageCreator` manages the creation of the image.
   - **Open-Closed Principle**: The image creation logic can be extended by adding new methods to `ImageCreator` or new settings to `ImageConfig` without modifying existing code.
   - **Liskov Substitution Principle**: Future subclasses of `ImageCreator` could easily replace the existing one without altering how the rest of the program functions.
   - **Inversion of Control**: The configuration settings are injected into the `ImageCreator`, adhering to dependency injection principles.
   - **Dependency Injection**: The `ImageCreator` receives its configuration via the constructor.

2. **GoF Design Patterns**:
   - **Facade Pattern**: The `ImageCreator` serves as a facade that encapsulates the complexity of image creation, enabling a simpler interface for users.
   - **Builder Pattern (indirectly used)**: The separate construction of the `ImageConfig` object allows for more complex configurations in the future.
  
3. **Environment Variables**: 
   - All configurable settings are stored in a `.env` file, which allows for easy changes without modifying the code.

### Step 4: Create the `.env` File

Create a file named `.env` in the same directory as the script, containing:

```
FONT_PATH=Python-Scripts/Text-to-Image/fonts/Roboto-Black.ttf
IMAGE_SIZE=1920,1080
BACKGROUND_COLOR=#FFFFFF
TEXT_COLOR=#FF0000
FONT_SIZE=40
```
