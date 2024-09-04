import os
from os.path import join
from PIL import Image

# .env file content
"""
INPUT_FOLDER=<Add input folder>
OUTPUT_FOLDER=<Add output folder>
WATERMARK_IMAGE=<Add watermark image>
BASE_WIDTH=2048
"""

class WatermarkConfig:
    """Singleton class to manage configuration."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WatermarkConfig, cls).__new__(cls)
            cls._instance.input_folder = os.getenv('INPUT_FOLDER')
            cls._instance.output_folder = os.getenv('OUTPUT_FOLDER')
            cls._instance.watermark_image = os.getenv('WATERMARK_IMAGE')
            cls._instance.base_width = int(os.getenv('BASE_WIDTH', 2048))
        return cls._instance


class ImageProcessor:
    """Class to manage image processing and watermarking."""

    def __init__(self, infolder, outfolder, watermark):
        self.infolder = infolder
        self.outfolder = outfolder
        self.watermark = watermark

    def apply_watermark(self, image_path):
        """Method to apply watermark to a single image."""
        try:
            im = Image.open(image_path)
            mark = Image.open(self.watermark)

            position = (im.size[0] - (mark.size[0] + 50),
                        im.size[1] - (mark.size[1] + 50))

            layer = Image.new('RGBA', im.size, (0, 0, 0, 0))
            layer.paste(mark, position)

            new_image = Image.composite(layer, im, layer)
            self.resize_and_save(new_image, im.filename)

        except Exception as error:
            print(f'Caught this error: {repr(error)}')

    def resize_and_save(self, image, original_filename):
        """Resize and save the watermarked image."""
        wpercent = (WatermarkConfig().base_width / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image_resized = image.resize(
            (WatermarkConfig().base_width, hsize), Image.ANTIALIAS
        )
        output_path = join(self.outfolder, f'with-watermark_{os.path.basename(original_filename)}')
        image_resized.save(output_path, 'jpeg')


class WatermarkBatchProcessor:
    """Facade for batch processing of images."""

    def __init__(self, config):
        self.config = config
        self.processor = ImageProcessor(
            config.input_folder,
            config.output_folder,
            config.watermark_image
        )

    def run(self):
        """Execute the batch processing of images."""
        for root, dirs, files in os.walk(self.config.input_folder):
            for name in files:
                image_path = join(root, name)
                self.processor.apply_watermark(image_path)


if __name__ == '__main__':
    config = WatermarkConfig()
    batch_processor = WatermarkBatchProcessor(config)
    batch_processor.run()
