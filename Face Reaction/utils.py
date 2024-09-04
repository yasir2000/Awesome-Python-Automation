import os
import cv2
import numpy as np
from dotenv import load_dotenv

load_dotenv()

def get_camera_index():
    return int(os.getenv('CAMERA_INDEX', 0))

def get_frame_dimensions():
    return (int(os.getenv('FRAME_WIDTH', 640)), int(os.getenv('FRAME_HEIGHT', 480)))

def get_emoji_paths():
    import json
    return json.loads(os.getenv('EMOJI_PATHS', '{}'))

def load_emoji(emotion):
    paths = get_emoji_paths()
    image_url = paths.get(emotion, paths["none"])
    return cv2.imread(image_url)
