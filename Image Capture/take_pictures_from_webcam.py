#!/usr/bin/env python3

import cv2
import click
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class VideoCaptureFactory:
    @staticmethod
    def create_capture(source=0):
        return cv2.VideoCapture(source)

class FrameProcessor:
    def __init__(self, name, directory):
        self.name = name
        self.directory = directory
        self.frame_count = 0

    def process_frame(self, frame):
        frame_resized = cv2.resize(frame, (600, 600))
        return frame_resized

    def save_frame(self, frame):
        file_path = os.path.join(self.directory, f"{self.name}{self.frame_count}.jpg")
        cv2.imwrite(file_path, frame)
        print(f"Saved {file_path}")
        self.frame_count += 1

class FrameCaptureCommand:
    def __init__(self, frame_processor):
        self.frame_processor = frame_processor

    def execute(self, frame):
        processed_frame = self.frame_processor.process_frame(frame)
        self.frame_processor.save_frame(processed_frame)

class FrameViewer:
    def __init__(self, capture_object, frame_capture_command):
        self.capture = capture_object
        self.command = frame_capture_command

    def start_viewing(self):
        while True:
            ret, frame = self.capture.read()
            if not ret:
                break

            cv2.imshow("Frame", frame)
            key = cv2.waitKey(50)

            if key & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break

            if key & 0xFF == ord(" "):
                self.command.execute(frame)

@click.command()
@click.option("--directory", default=os.getenv("FRAME_DIR", os.getcwd()), help="Directory to store frames")
@click.option("--name", default=os.getenv("FRAME_NAME", "person"), help="Base name for saved frames")
def main(name, directory):
    capture = VideoCaptureFactory.create_capture()
    frame_processor = FrameProcessor(name, directory)
    frame_capture_command = FrameCaptureCommand(frame_processor)
    viewer = FrameViewer(capture, frame_capture_command)
    viewer.start_viewing()
    capture.release()

if __name__ == "__main__":
    main()
