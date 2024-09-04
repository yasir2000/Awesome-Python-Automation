
### Directory Structure
```
emotion_recognition/
│
├── .env
├── emotion_detector.py
├── emotion_manager.py
├── main.py
└── utils.py
```

### .env
```env
CAMERA_INDEX=0
FRAME_WIDTH=640
FRAME_HEIGHT=480
EMOJI_SIZE=150
EMOJI_PATHS={
    "angry": "https://i.ibb.co/QN0gqNH/angry.png",
    "disgust": "https://i.ibb.co/tJDxrhD/disgust.png",
    "fear": "https://i.ibb.co/yBczSFB/fear.png",
    "happy": "https://i.ibb.co/g6DW0Cf/happy.png",
    "sad": "https://i.ibb.co/NyF0sDq/sad.png",
    "surprise": "https://i.ibb.co/D4rDyfM/surprise.png",
    "neutral": "https://i.ibb.co/KX7VSjh/neutral.png",
    "none": "https://i.ibb.co/LdnS9nL/none.png"
}
```


### Breakdown of Changes
1. **Single Responsibility Principle**: Code is separated into three classes (`EmotionManager`, `EmotionDetector`, and utility functions in `utils.py`), each managing distinct responsibilities.
   
2. **Open/Closed Principle**: The design allows for easy extensions, such as adding new emotions and their corresponding paths without modifying the existing code.

3. **Liskov Substitution Principle**: Each class can be replaced or extended without altering system functionality.

4. **Dependency Inversion**: The main logic does not rely on concrete implementations but on abstractions (like loading configurations).

5. **GoF Design Patterns**: 
   - **Facade**: The `EmotionManager` acts as a facade for managing emotions and their visual representations.
   - **Strategy**: The `EmotionDetector` can be extended to use different emotion-detection techniques in the future.

6. **Environment Variables**: Used to manage configurations such as camera index, frame dimensions, and emoji paths.

