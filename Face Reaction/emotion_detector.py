from fer import FER

class EmotionDetector:
    def __init__(self):
        self.detector = FER(mtcnn=True)

    def detect_emotion(self, frame):
        return self.detector.top_emotion(frame)
