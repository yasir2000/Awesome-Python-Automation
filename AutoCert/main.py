import os
from PIL import Image, ImageFont, ImageDraw
import pandas as pd
from abc import ABC, abstractmethod
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class CertificateConfig:
    def __init__(self):
        self.name_font_path = os.getenv("NAME_FONT_PATH", "fonts/Roboto-Light.ttf")
        self.id_font_path = os.getenv("ID_FONT_PATH", "fonts/orbitron-black.otf")
        self.name_size = int(os.getenv("NAME_SIZE", 60))
        self.id_size = int(os.getenv("ID_SIZE", 48))
        self.name_location = tuple(map(float, os.getenv("NAME_LOCATION", "1260.5,811.5").split(',')))
        self.id_location = tuple(map(float, os.getenv("ID_LOCATION", "1326,1369").split(',')))
        self.event_id = os.getenv("EVENT_ID", "Event")
        self.output_path = os.getenv("OUTPUT_PATH", "exports/")

class CertificateGenerator:
    def __init__(self, config: CertificateConfig):
        self.config = config
        self.name_font = ImageFont.truetype(self.config.name_font_path, size=self.config.name_size)
        self.id_font = ImageFont.truetype(self.config.id_font_path, size=self.config.id_size)

    def generate_certificates(self, name_list):
        for i, name in enumerate(name_list):
            self._create_certificate(name, i + 1)

    def _create_certificate(self, name, index):
        im = Image.open("Sample.png")
        draw = ImageDraw.Draw(im)
        text_color = (63, 61, 86)

        # Draw Name
        name_width, name_height = draw.textsize(name, font=self.name_font)
        draw.text((self.config.name_location[0] - name_width / 2, self.config.name_location[1] - name_height / 2), 
                   name, font=self.name_font, fill=text_color)

        # Draw ID
        cert_id = f"{self.config.event_id}{index}"
        draw.text(self.config.id_location, cert_id, font=self.id_font, fill=text_color)

        # Save Certificate
        rgb = Image.new('RGB', im.size, (255, 255, 255))
        rgb.paste(im, mask=im.split()[3])
        rgb.save(f"{self.config.output_path}{name}.pdf", 'PDF', resolution=100.0)

class DataLoader:
    @staticmethod
    def load_data(file_path):
        return pd.read_csv(file_path, names=['names']).names.tolist()

def main():
    config = CertificateConfig()
    name_list = DataLoader.load_data('names.csv')
    
    generator = CertificateGenerator(config)
    generator.generate_certificates(name_list)

if __name__ == "__main__":
    main()
