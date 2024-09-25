import os
import cv2
import numpy as np
import time
from dotenv import load_dotenv
import mediapipe as mp

# Load environment variables
load_dotenv()

# ----- Constants and Configuration -----
class Config:
    VIDEO_SOURCE = int(os.getenv('VIDEO_SOURCE', 0))
    TOOL_IMAGE = os.getenv('TOOL_IMAGE', "tools.png")
    CANVAS_WIDTH = int(os.getenv('CANVAS_WIDTH', 640))
    CANVAS_HEIGHT = int(os.getenv('CANVAS_HEIGHT', 480))
    LINE_THICKNESS = int(os.getenv('LINE_THICKNESS', 4))
    RADIUS = int(os.getenv('RADIUS', 40))
    DETECTION_CONFIDENCE = float(os.getenv('DETECTION_CONFIDENCE', 0.6))


# ----- Hand Tracking and Drawing Utilities -----
class HandTracker:
    def __init__(self):
        self.hands = mp.solutions.hands
        self.hand_landmark = self.hands.Hands(min_detection_confidence=Config.DETECTION_CONFIDENCE,
                                               min_tracking_confidence=Config.DETECTION_CONFIDENCE,
                                               max_num_hands=1)
        self.draw = mp.solutions.drawing_utils

    def process_frame(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return self.hand_landmark.process(rgb_frame)


class VirtualPainter:
    def __init__(self):
        self.tools_image = self.load_tools_image()
        self.mask = self.create_empty_mask()
        self.curr_tool = "select tool"
        self.time_init = True
        self.prev_x, self.prev_y = 0, 0
        self.var_inits = False
        self.rad = Config.RADIUS

    def load_tools_image(self):
        return cv2.imread(Config.TOOL_IMAGE).astype('uint8')

    def create_empty_mask(self):
        return np.ones((Config.CANVAS_HEIGHT, Config.CANVAS_WIDTH)) * 255

    def handle_draw(self, landmarks):
        # Handle drawing based on the current tool
        x = int(landmarks[8].x * Config.CANVAS_WIDTH)
        y = int(landmarks[8].y * Config.CANVAS_HEIGHT)

        if self.curr_tool == "draw":
            self.draw_on_mask(x, y)

        # Additional tools implementation
        func = getattr(self, f'handle_{self.curr_tool}', None)
        if func:
            func(landmarks, x, y)

    def draw_on_mask(self, x, y):
        cv2.circle(self.mask, (x, y), Config.RADIUS, 0, Config.LINE_THICKNESS)

    def handle_line(self, landmarks, x, y):
        xi, yi = int(landmarks[12].x * Config.CANVAS_WIDTH), int(landmarks[12].y * Config.CANVAS_HEIGHT)
        if self.indicators_raised(yi, landmarks[9].y):
            if not self.var_inits:
                self.xii, self.yii = x, y
                self.var_inits = True
            cv2.line(self.mask, (self.xii, self.yii), (x, y), 0, Config.LINE_THICKNESS)
            
    def handle_rectangle(self, landmarks, x, y):
        # Rectangle drawing logic
        xi, yi = int(landmarks[12].x * Config.CANVAS_WIDTH), int(landmarks[12].y * Config.CANVAS_HEIGHT)
        if self.indicators_raised(yi, landmarks[9].y):
            if not self.var_inits:
                self.xii, self.yii = x, y
                self.var_inits = True
            cv2.rectangle(self.mask, (self.xii, self.yii), (x, y), 0, Config.LINE_THICKNESS)
    def handle_circle(self, landmarks, x, y):
        xi, yi = int(landmarks[12].x * Config.CANVAS_WIDTH), int(landmarks[12].y * Config.CANVAS_HEIGHT)
        if self.indicators_raised(yi, landmarks[9].y):
            if not self.var_inits:
                self.xii, self.yii = x, y
                self.var_inits = True
            radius = int(((self.xii - x) ** 2 + (self.yii - y) ** 2) ** 0.5)
            cv2.circle(self.mask, (self.xii, self.yii), radius, 0, Config.LINE_THICKNESS)

    def handle_erase(self, landmarks, x, y):
        cv2.circle(self.mask, (x, y), 30, 255, -1)  # Erase effect

    def get_tool(self, x):
        if x < 50:
            return "line"
        elif x < 100:
            return "rectangle"
        elif x < 150:
            return "draw"
        elif x < 200:
            return "circle"
        else:
            return "erase"

    def indicators_raised(self, yi, y9):
        return (y9 - yi) > 40

    def update_tool(self, x):
        if self.time_init:
            self.ctime = time.time()
            self.time_init = False
        ptime = time.time()

        if (ptime - self.ctime) > 0.8:
            self.curr_tool = self.get_tool(x)
            print("Your current tool is set to:", self.curr_tool)
            self.time_init = True
            self.rad = Config.RADIUS

    def process_frame(self, frame):
        frame = cv2.flip(frame, 1)
        op = hand_tracker.process_frame(frame)

        if op.multi_hand_landmarks:
            for hand_landmarks in op.multi_hand_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
                x = int(hand_landmarks.landmark[8].x * Config.CANVAS_WIDTH)
                y = int(hand_landmarks.landmark[8].y * Config.CANVAS_HEIGHT)

                if 0 <= x < Config.CANVAS_WIDTH and 0 <= y < Config.CANVAS_HEIGHT:
                    self.update_tool(x)
                    self.handle_draw(hand_landmarks.landmark)

        # Apply the mask to the frame
        frame_result = cv2.bitwise_and(frame, frame, mask=self.mask)
        return frame_result


# ----- Application Entry Point -----
if __name__ == "__main__":
    cap = cv2.VideoCapture(Config.VIDEO_SOURCE)
    hand_tracker = HandTracker()
    painter = VirtualPainter()

    while True:
        success, frm = cap.read()
        if not success:
            break
        
        processed_frame = painter.process_frame(frm)

        # Overlay tools image
        tools_region = processed_frame[:Config.CANVAS_HEIGHT, 0:250]
        tools_image = cv2.addWeighted(painter.tools_image, 0.7, tools_region, 0.3, 0)
        processed_frame[:Config.CANVAS_HEIGHT, 0:250] = tools_image

        # Display current tool text
        cv2.putText(processed_frame, painter.curr_tool, (270, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.namedWindow("Virtual Painter", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Virtual Painter", 1500, 900)
        cv2.imshow("Virtual Painter", processed_frame)

        if cv2.waitKey(1) == 27:  # ESC to exit
            cv2.destroyAllWindows()
            cap.release()
            break
