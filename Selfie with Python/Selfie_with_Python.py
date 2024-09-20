import cv2
import time
import os
from abc import ABC, abstractmethod

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Constants from environment variables
CAMERA_INDEX = int(os.getenv('CAMERA_INDEX', 0))
IMAGE_DIR = os.getenv('IMAGE_DIR', './selfies')

# Abstract Factory for creating a Camera
class CameraFactory(ABC):
    @abstractmethod
    def create_camera(self) -> cv2.VideoCapture:
        pass

class DefaultCameraFactory(CameraFactory):
    def create_camera(self) -> cv2.VideoCapture:
        return cv2.VideoCapture(CAMERA_INDEX)


# Interface for taking selfies
class SelfieTaker(ABC):
    @abstractmethod
    def take_selfie(self):
        pass

class CameraSelfieTaker(SelfieTaker):
    def __init__(self, camera):
        self.camera = camera
        self.img_count = 0

    def take_selfie(self):
        cv2.namedWindow("Take selfie with python")

        while True:
            ret, frame = self.camera.read()
            if not ret:
                print("Failed to grab frame")
                break

            cv2.imshow("Take selfie with python", frame)

            k = cv2.waitKey(1)

            if k % 256 == 27:  # Escape key
                print("Escape hit, closing the window")
                break

            if k % 256 == 32:  # Space key
                img_name = f"{IMAGE_DIR}/Selfie_{self.img_count}.jpg"
                cv2.imwrite(img_name, frame)
                print(f"Selfie taken: {img_name}")
                self.img_count += 1

        self.camera.release()
        cv2.destroyAllWindows()


# Main application class
class SelfieApp:
    def __init__(self, selfie_taker: SelfieTaker):
        self.selfie_taker = selfie_taker

    def run(self):
        print("Press Space-bar to click Selfie")
        print("Press Escape key to terminate the window")
        time.sleep(5)
        self.selfie_taker.take_selfie()

# Entry point
if __name__ == "__main__":
    # Instantiate factory to create camera
    camera_factory = DefaultCameraFactory()
    camera = camera_factory.create_camera()

    # Use Dependency Injection via constructor
    selfie_taker = CameraSelfieTaker(camera)
    app = SelfieApp(selfie_taker)
    app.run()
