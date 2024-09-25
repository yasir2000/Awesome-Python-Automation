import os
import random
import requests
import ctypes
import numpy as np
from PIL import Image, ImageFont, ImageDraw
import yfinance as yf
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class QuoteFetcher:
    API_URL = os.getenv("QUOTE_API_URL", "http://api.quotable.io/random")

    def fetch_quote(self):
        try:
            response = requests.get(self.API_URL)
            response.raise_for_status()
            quote_data = response.json()
            return f"{quote_data['content']} - {quote_data['author']}"
        except Exception as e:
            print(f"Error fetching quote: {e}")
            return None

class ImageProcessor:
    def __init__(self, font_path):
        self.font_path = font_path

    def add_margin(self, img, top, left, bottom, right, color):
        width, height = img.size
        new_width = width + right + left
        new_height = height + top + bottom
        result = Image.new(img.mode, (new_width, new_height), color)
        result.paste(img, (left, top))
        return result

    def resize_to_fit(self, path, path_to_save=None):
        img = Image.open(path)
        if img.size[0] / 1920 > img.size[1] / 1080:
            vres = int((img.size[0] * 1080 / 1920 - img.size[1]) / 2)
            img = self.add_margin(img, vres, 0, vres, 0, (0, 0, 0))
        else:
            hres = int((img.size[1] * 1920 / 1080 - img.size[0]) / 2)
            img = self.add_margin(img, 0, hres, 0, hres, (0, 0, 0))
        
        if path_to_save:
            img.save(path_to_save)
        else:
            img.save(path)

class TickerRenderer:
    def __init__(self, tickers):
        self.tickers = tickers

    def get_price_change(self, ticker):
        stock = yf.Ticker(ticker)
        history = stock.history(period="3d")
        change = ((history.iloc[-1]["Close"] - history.iloc[-2]["Close"]) / history.iloc[-2]["Close"]) * 100
        return round(change, 2), round(history.iloc[-1]["Close"], 2)

    def render_tickers(self, draw, font, start_pos):
        for i, (symbol, name) in enumerate(self.tickers):
            change, price = self.get_price_change(symbol)
            color = (0, 255, 0) if change >= 0 else (255, 0, 0)
            draw.text((1670, start_pos + i * 25), name, font=font, fill=(255, 255, 255))
            draw.text((1750, start_pos + i * 25), f"{abs(change):.2f}%", font=font, fill=color)
            draw.text((1830, start_pos + i * 25), str(price), font=font, fill=color)

class WallpaperManager:
    def __init__(self, image, save_path):
        self.image = image
        self.save_path = save_path

    def save_and_set_wallpaper(self):
        try:
            self.image.save(self.save_path, quality="high")
            ctypes.windll.user32.SystemParametersInfoW(20, 0, self.save_path, 0)
        except Exception as e:
            print(f"Error saving wallpaper: {e}")

def main():
    enable_time = os.getenv("ENABLE_TIME", "true").lower() == "true"
    enable_tickers = os.getenv("ENABLE_TICKERS", "true").lower() == "true"
    enable_quote = os.getenv("ENABLE_QUOTE", "true").lower() == "true"

    current_time = datetime.now().strftime("%H:%M:%S  )")

    tickers = [
        ("^GSPC", "S&P 500"),
        ("AAPL", "AAPL"),
        ("MSFT", "MSFT"),
        ("GOOGL", "GOOGL"),
        ("AMZN", "AMZN"),
        ("TSLA", "TSLA"),
        ("BTC-USD", "BTC"),
        ("ETH-USD", "ETH")
    ]

    image_folder = os.getenv("IMAGE_FOLDER", "path/to/folder/containing/images/")
    font_path = os.getenv("FONT_PATH", "path/to/.ttf/font/file")
    save_path = os.getenv("SAVE_PATH", "path/to/save/temp/wallpaper/in/image.jpg")

    # Select a random image from the folder
    images = os.listdir(image_folder)
    selected_image_path = os.path.join(image_folder, random.choice(images))
    
    # Initialize the processors
    image_processor = ImageProcessor(font_path)
    quote_fetcher = QuoteFetcher()
    ticker_renderer = TickerRenderer(tickers)

    # Process the selected image
    image_processor.resize_to_fit(selected_image_path, None)
    img = Image.open(selected_image_path).resize((1920, 1080))
    
    # Start drawing
    draw = ImageDraw.Draw(img)
    
    # Add quote if enabled
    if enable_quote:
        quote = quote_fetcher.fetch_quote()
        if quote:
            my_font = ImageFont.truetype(font_path, 20)
            draw.text((10, 1050), quote, font=my_font, fill=(255, 255, 255))
    
    # Add current time if enabled
    if enable_time:
        draw.text((1830, 1050), current_time, font=my_font, fill=(255, 255, 255))

    # Render ticker information if enabled
    if enable_tickers:
        ticker_renderer.render_tickers(draw, my_font, 10)

    # Save wallpaper and set it
    wallpaper_manager = WallpaperManager(img, save_path)
    wallpaper_manager.save_and_set_wallpaper()

if __name__ == "__main__":
    main()
