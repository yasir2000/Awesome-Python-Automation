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
