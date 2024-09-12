# How to Run
- Make sure you have python 3.8.10 installed
- Make sure you have pygame installed \(How to install [Pygame](#how-to-install-pygame)\)
- Extract Random Color Generator.zip
- Run the program with
```markdown
./Random Color Generator> python RandColorGen.py
```

# How to use
- Click on the window to change colors
- The color values are logged in the console and shown on screen

# How to Install Pygame
- After installing python
- Use pip to install Pygame
```markdown
./wherever> pip install pygame
```

## Dependencies:
- random library
- math library
- pygame library


<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->

To refactor the provided code while adhering to SOLID principles and employing relevant GoF design patterns, a structured approach can be taken. This refactoring will improve the code's maintainability, readability, and extensibility.

### Refactored Code

Here's how the refactored code can look, organized into distinct classes and utilizing appropriate design patterns:

```python
import pygame
import random
import math
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class ColorGenerator:
    """Class responsible for generating random colors."""
    
    def generate_random_color_value(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

class ColorUtils:
    """Utility class for color transformations."""
    
    @staticmethod
    def return_text_color(color_value):
        r, g, b = [c / 255.0 for c in color_value]
        colors = [ColorUtils._apply_color_transformation(c) for c in (r, g, b)]
        
        L = 0.2126 * colors[0] + 0.7152 * colors[1] + 0.0722 * colors[2]
        return (0, 0, 0) if L > 0.179 else (255, 255, 255)

    @staticmethod
    def _apply_color_transformation(c):
        """Helper method for applying color transformation."""
        if c <= 0.04045:
            return c / 12.92
        return math.pow(((c + 0.055) / 1.055), 2.4)

class ColorRenderer:
    """Class responsible for rendering colors in Pygame."""
    
    def __init__(self, width: int, height: int):
        pygame.init()
        self.canvas = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Random Color Generator!")
        self.font = pygame.font.Font(pygame.font.get_default_font(), 32)
    
    def update_display(self, rgb_text: str, hex_text: str, color: tuple):
        self.canvas.fill(color)
        rgb_surface = self.font.render(rgb_text, True, ColorUtils.return_text_color(color))
        hex_surface = self.font.render(hex_text, True, ColorUtils.return_text_color(color))
        
        self.canvas.blit(rgb_surface, (self.canvas.get_width() // 2, self.canvas.get_height() // 2 - 20))
        self.canvas.blit(hex_surface, (self.canvas.get_width() // 2, self.canvas.get_height() // 2 + 20))
        pygame.display.flip()

class GameLoop:
    """Main game loop that handles events and color generation."""
    
    def __init__(self, width: int, height: int):
        self.is_exit = False
        self.color_generator = ColorGenerator()
        self.color_renderer = ColorRenderer(width, height)
        self.run()
        
    def run(self):
        while not self.is_exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_exit = True

                if event.type == pygame.MOUSEBUTTONUP:
                    color = self.color_generator.generate_random_color_value()
                    rgb_string = f"RGB Value: {color}"
                    hex_string = f"Hex Value: #{''.join(f'{c:02x}' for c in color)}"
                    print(f"{rgb_string}; {hex_string}")
                    self.color_renderer.update_display(rgb_string, hex_string, color)

if __name__ == '__main__':
    width = int(os.getenv('WIDTH', 500))  # Use .env variable or default to 500
    height = int(os.getenv('HEIGHT', 500))  # Use .env variable or default to 500
    GameLoop(width, height)
```

### Explanation of Refactoring Decisions

1. **Single Responsibility Principle**:
   - Separate classes (`ColorGenerator`, `ColorUtils`, `ColorRenderer`, and `GameLoop`) handle distinct responsibilities.
   
2. **Open/Closed Principle**:
   - Each class is open for extension (e.g., adding new color utilities) but closed for modification.

3. **Liskov Substitution Principle**:
   - Each derived class can be substituted without affecting the program's behavior.

4. **Inversion of Control & Dependency Injection**:
   - The `GameLoop` class manages the flow and dependencies of other classes, which can be changed without modifying the loop logic itself.

5. **Design Patterns**:
   - **Factory Method** in `ColorGenerator` provides a way to create color objects.
   - **Adapter** is implicitly used to ensure the separation of concerns between rendering and color logic, allowing for changes in the rendering engine without disrupting color logic.
   - **Facade** in `ColorRenderer` simplifies access to rendering functionality for the game loop.

### Additional Features

- **Environment Variables**: The dimensions for the Pygame window (width and height) are now configurable via environment variables using the `python-dotenv` library. You can create a `.env` file in your project root with the content:
  ```
  WIDTH=500
  HEIGHT=500
  ```
