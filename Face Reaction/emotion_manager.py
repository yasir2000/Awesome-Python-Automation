class EmotionManager:
    def __init__(self):
        self.emoji_paths = get_emoji_paths()

    def get_emoji(self, emotion):
        emoji = self.emoji_paths.get(emotion, self.emoji_paths["none"])
        return cv2.imread(emoji)

    def annotate_frame(self, frame, emotion):
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (40, 210)
        fontScale = 1
        color = (255, 0, 0)
        thickness = 2
        cv2.putText(frame, emotion, org, font, fontScale, color, thickness, cv2.LINE_AA)
