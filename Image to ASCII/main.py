import os
from PIL import Image
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class AsciiArtGenerator:
    def __init__(self, new_width):
        self.new_width = new_width
        self.ascii_chars = os.getenv("ASCII_CHARS", "@#S%?*+;:,.").split(",")

    def resize_image(self, image):
        width, height = image.size
        ratio = height / width
        new_height = int(self.new_width * ratio)
        return image.resize((self.new_width, new_height))

    def grayify(self, image):
        return image.convert("L")

    def pixels_to_ascii(self, image):
        pixels = image.getdata()
        return "".join([self.ascii_chars[pixel // (256 // len(self.ascii_chars))] for pixel in pixels])

    def generate_ascii(self, image_path):
        try:
            image = Image.open(image_path)
        except Exception as e:
            raise ValueError(f"{image_path} is not a valid pathname to an image.") from e

        # Process image
        new_image_data = self.pixels_to_ascii(self.grayify(self.resize_image(image)))

        # Format ASCII output
        pixel_count = len(new_image_data)
        return "\n".join([new_image_data[index:(index + self.new_width)] for index in range(0, pixel_count, self.new_width)])

    def save_to_file(self, ascii_image, output_path):
        with open(output_path, "w") as f:
            f.write(ascii_image)


class AsciiArtApp:
    def __init__(self, generator):
        self.generator = generator

    def run(self):
        path = input("Enter a valid pathname to an image:\n")
        try:
            ascii_image = self.generator.generate_ascii(path)
            print(ascii_image)
            self.generator.save_to_file(ascii_image, os.getenv("OUTPUT_PATH", "ascii_image/ascii_image.txt"))
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    new_width = int(os.getenv("NEW_WIDTH", 100))
    generator = AsciiArtGenerator(new_width)
    app = AsciiArtApp(generator)
    app.run()
