import glob
import os
from PIL import Image
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class ImageLoader:
    """Factory Method to load images from a specified folder."""
    
    def __init__(self, frame_folder):
        self.frame_folder =_folder

    def load_images(self):
        """Load images from the specified folder."""
        frame_files = glob.glob(os.path.join(self.frame_folder, "*.JPG"))
        return [Image.open(image) for image in frame_files]

class GIFBuilder:
    """Builder to construct a GIF from loaded images."""
    
    def __init__(self, images):
        self.images = images

    def save_gif(self, output_filename="my_awesome.gif", duration=100):
        """Save images as a GIF."""
        if not self.images:
            raise ValueError("No images available to create a GIF.")
        
        frame_one = self.images[0]
        frame_one.save(
            output_filename,
            format="GIF",
            append_images=self.images,
            save_all=True,
            duration=duration,
            loop=0
        )

class GIFCreator:
    """Facade that provides a simplified interface to create a GIF from images."""
    
    def __init__(self, frame_folder):
        self.loader = ImageLoader(frame_folder)
    
    def create_gif(self, output_filename="my_awesome.gif", duration=100):
        images = self.loader.load_images()
        builder = GIFBuilder(images)
        builder.save_gif(output_filename, duration)

if __name__ == "__main__":
    frame_folder = os.getenv("FRAME_FOLDER", "/path/to/images")
    gif_creator = GIFCreator(frame_folder)
    gif_creator.create_gif()

