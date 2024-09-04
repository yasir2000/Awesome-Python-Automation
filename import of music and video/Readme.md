**ABOUT**
# Music Player

A simple Python script that provides a graphical user interface (GUI) for playing music files. This script uses `tkinter` for the GUI and `pygame` for audio playback.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python3 installed.
- The `pygame` library installed. You can install it using pip:

   ```bash
   pip install pygame


## Usage
Clone or download this repository to your local machine.
Open your terminal or command prompt and navigate to the project directory.

Run the script using Python:
bash
python music_player.py
Click the "Open Music File" button to select an MP3 or WAV music file from your computer.

The selected music file will be played using the pygame mixer.


**Troubleshooting**
If you encounter any issues while using the music player, please consider the following troubleshooting steps:

1. Ensure you have Python 3 installed.
2. Verify that pygame is installed by running pip show pygame.
3. Check your system's audio settings for playback.

------------------------------------------------------------------------------------------------------------------------------------------

**README.md for Video Player Script:**

# Video Player

A Python script that provides a graphical user interface (GUI) for playing video files (MP4 or AVI). This script uses `tkinter` for the GUI and relies on the [OpenCV](https://opencv.org/) library for video playback.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3 installed.
- The [OpenCV](https://opencv.org/) library installed. You can install it using pip:

   ```bash
   pip install opencv-python

**Usage**
Clone or download this repository to your local machine.
Open your terminal or command prompt and navigate to the project directory.

Run the script using Python:
bash
python video_player.py
Click the "Open Video File" button to select an MP4 or AVI video file from your computer.

The selected video file will be played using the OpenCV-based video player.


**Troubleshooting**
If you encounter any issues while using the video player, please consider the following troubleshooting steps:

1. Ensure you have Python 3 installed.
2. Verify that opencv-python is installed by running pip show opencv-python.
3. Check your system's video codec support and audio settings.


<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->

Refactoring the provided code while implementing the SOLID principles and the GoF design patterns can lead to a more maintainable and scalable structure. Below, I’ll create a more modular music and video player that adheres to these principles, while also using environment variables for configuration.

### Directory Structure and Environment Variables
First, create a `.env` file for configuration:

```plaintext
MUSIC_DIRECTORY="./music"
VIDEO_DIRECTORY="./videos"
```


### Explanation of Design Patterns and Principles Used

1. **Single Responsibility Principle**: The functionality of listing files, playing, stopping music, and video is encapsulated in their respective classes.
  
2. **Open/Closed Principle**: The player classes can be extended with new functionalities without modifying existing code.

3. **Liskov Substitution Principle**: Both `MusicPlayer` and `VideoPlayer` can be used interchangeably where a `BasePlayer` is expected.

4. **Dependency Injection**: The `PlayerUI` class uses composition to include `MusicPlayer` and `VideoPlayer`.

5. **GoF Design Patterns**: 
   - **Adapter**: The `PlayerUI` adapts different player classes for music and video.
   - **Factory Method**: The directories can be selected based on media type when choosing.

