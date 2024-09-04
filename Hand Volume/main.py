import os
import numpy as np
import cv2
import time
import math
from handTrackingModule import HandDetector
from interface import AudioController
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
width = int(os.getenv("CAMERA_WIDTH", 640))
height = int(os.getenv("CAMERA_HEIGHT", 480))
frame_reduction = int(os.getenv("FRAME_REDUCTION", 100))
smoothening = int(os.getenv("SMOOTHENING", 7))
volume_db = float(os.getenv("VOLUME_DB", -65.25))
volume_percent_scale = float(os.getenv("VOLUME_PERCENT_SCALE", 50))

class VolumeControl:
    def __init__(self):
        self.audio_controller = AudioController()

    def set_volume(self, percent):
        change_volume = round((math.log((percent / 10) + 1) * volume_percent_scale) * 0.54)
        self.audio_controller.set_master_volume(volume_db + change_volume)

class VideoCapture:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, width)
        self.cap.set(4, height)
        
    def get_frame(self):
        return self.cap.read()
    
    def release(self):
        self.cap.release()

def main():
    detector = HandDetector(detectionCon=0.75)
    volume_control = VolumeControl()
    video_capture = VideoCapture()
    plocX, plocY, clocX, clocY = 0, 0, 0, 0

    while True:
        success, img = video_capture.get_frame()
        img = detector.find_hands(img)
        lm_list = detector.find_position(img)
        fingers = []
        
        if lm_list:
            # Finger detection logic
            # Process fingers and volume adjustment
            x_thumb, y_thumb = lm_list[4][1], lm_list[4][2]
            x_index, y_index = lm_list[8][1], lm_list[8][2]
            distance = math.sqrt((x_index - x_thumb)**2 + (y_index - y_thumb)**2)
            percent = round((distance - 50) / 2)
            percent = max(0, min(percent, 100))  # Limit percentage

            volume_control.set_volume(percent)

            # Draw on the image
            cv2.circle(img, (x_index, y_index), 15, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x_thumb, y_thumb), 15, (0, 0, 255), cv2.FILLED)

        # Update frame and display 
        cv2.imshow("Hand Tracking", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
