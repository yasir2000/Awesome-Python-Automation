# .env
# This file would contain environment variables.
FONT_PATH="Python-Scripts/Text-to-Image/fonts/Roboto-Black.ttf"
IMAGE_SIZE="1920,1080"
BACKGROUND_COLOR="#FFFFFF"
TEXT_COLOR="#FF0000"
FONT_SIZE=40

import os
from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv

class ImageConfig:
    """Configuration class for image settings."""
    
    def __init__(self):
        self.font_path = os.getenv("FONT_PATH")
        self.image_size = tuple(map(int, os.getenv("IMAGE_SIZE").split(',')))
        self.background_color = os.getenv("BACKGROUND_COLOR", "#FFFFFF")
        self.text_color = os.getenv("TEXT_COLOR", "#FF0000")
        self.font_size = int(os.getenv("FONT_SIZE", 40))

class ImageCreator:
    """Class responsible for creating images."""
    
    def __init__(self, config: ImageConfig):
        self.config = config

    def create_image(self, filename: str, text: str):
        """Create the image with specified text and filename."""
        img = Image.new(mode="RGB", size=self.config.image_size, color=self.config.background_color)
        d1 = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(self.config.font_path, self.config.font_size)
        d1.text((65, 10), text, fill=self.config.text_color, font=fnt)
        img.show()
        img.save(filename + ".jpeg")

def main():
    load_dotenv()  # Load environment variables
    filename = input("What would you like your image to be called? ")
    writing = input("Write your text here: ")

    config = ImageConfig()  # Initialize configuration
    image_creator = ImageCreator(config)  # Dependency injection
    image_creator.create_image(filename, writing)

if __name__ == '__main__':
    main()
