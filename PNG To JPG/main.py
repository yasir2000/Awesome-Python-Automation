import os
from PIL import Image
from glob import glob

# Load environment variables
IMAGE_DIRECTORY = os.getenv("IMAGE_DIRECTORY", ".")
OUTPUT_FORMAT = os.getenv("OUTPUT_FORMAT", "jpg")
QUALITY = int(os.getenv("QUALITY", 95))

class ImageProcessor:
    """Class responsible for processing images, adhering to Single Responsibility Principle."""
    
    def __init__(self, image_directory):
        self.image_directory = image_directory

    def get_image_files(self):
        """Facilitates retrieval of image files."""
        return glob(os.path.join(self.image_directory, "*.png"))

    def process_image(self, img_file):
        """Processes a single image file."""
        img = Image.open(img_file)  # Open the image file
        rgb_img = img.convert("RGB")  # Convert to RGB
        output_file = img_file.replace("png", OUTPUT_FORMAT)  # Change file extension
        rgb_img.save(output_file, quality=QUALITY)  # Save the image as .jpg or specified format

class ImageProcessorFacade:
    """Facade class to simplify image processing operations."""
    
    def __init__(self, image_processor):
        self.image_processor = image_processor

    def process_images(self):
        """Process all images in the specified directory."""
        img_files = self.image_processor.get_image_files()
        for img_file in img_files:
            self.image_processor.process_image(img_file)

if __name__ == "__main__":
    # Dependency Injection via constructor
    image_processor = ImageProcessor(image_directory=IMAGE_DIRECTORY)
    facade = ImageProcessorFacade(image_processor)
    facade.process_images()
