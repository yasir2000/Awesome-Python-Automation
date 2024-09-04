import cv2
from utils import get_camera_index, get_frame_dimensions
from emotion_manager import EmotionManager
from emotion_detector import EmotionDetector

def main():
    camera_index = get_camera_index()
    frame_width, frame_height = get_frame_dimensions()
    
    scr = cv2.VideoCapture(camera_index)
    scr.set(3, frame_width)
    scr.set(4, frame_height)

    emotion_detector = EmotionDetector()
    emotion_manager = EmotionManager()

    while True:
        ret, frame = scr.read()
        emotion, score = emotion_detector.detect_emotion(frame)
        print(emotion, score)

        emoj = emotion_manager.get_emoji(emotion)
        size = int(os.getenv('EMOJI_SIZE', 150))
        emoj = cv2.resize(emoj, (size, size))

        # Create mask
        img2gray = cv2.cvtColor(emoj, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
        roi = frame[-size-20:-20, -size-20:-20]

        roi[np.where(mask)] = 0
        roi += emoj

        emotion_manager.annotate_frame(frame, emotion)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    scr.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
