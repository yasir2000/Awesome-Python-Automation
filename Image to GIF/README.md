This repository consists of a list of python scripts to automate few tasks.

You can contribute by adding more python scripts which can be used to automate things. Some of already done are listed below.
Incase you have anything to be followed while executing the python script mention it as well


# Python Scripts

## Script  - Image-to-gif

Generate gif from Images
imageTogif.py

<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->

To refactor the provided code while adhering to SOLID principles and incorporating relevant GoF design patterns, we'll implement the following changes:

1. **Single Responsibility Principle**: Each class/function should have one responsibility.
2. **Open-Closed Principle**: The code should be open for extension but closed for modification.
3. **Liskov Substitution Principle**: We should ensure subclasses can replace their base class without affecting functionality.
4. **Dependency Inversion Principle**: High-level modules should not depend on low-level modules; both should depend on abstractions.
5. **Dependency Injection**: Inject dependencies rather than hardcoding them.

### Design Patterns to Apply

- **Factory Method**: Create an image loader.
- **Builder**: Construct the GIF.
- **Facade**: Simplify the interface for creating a GIF.


### .env Configuration

To make the frame folder configurable via environment variables, create a `.env` file containing:

```
FRAME_FOLDER=/path/to/images
```

### Explanation of Changes

1. **ImageLoader Class**: Implements the Factory Method pattern to load images.
2. **GIFBuilder Class**: Implements the Builder pattern to construct the GIF.
3. **GIFCreator Class**: Acts as a Facade, simplifying GIF creation for users by combining both `ImageLoader` and `GIFBuilder`.
4. **Environment Variables**: The path for image frames is now configurable through a `.env` file, adhering to Dependency Injection principles.

