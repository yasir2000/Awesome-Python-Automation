This python script is used for taking images from your webcam and saving it on your local device. Path to the folder can be specified using the following command:

> python3 take_pictures_from_webcam.py --directory pathname

The default path would be your current directory.  

You can also give name to your image using following command:
> python3 take_pictures_from_webcam.py --name ImageName

<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->

### Explanation of Refactor:

1. **SOLID Principles:**
   - **Single Responsibility Principle:** Each class (`VideoCaptureFactory`, `FrameProcessor`, `FrameCaptureCommand`, `FrameViewer`) has a distinct role: capturing video, processing frames, executing the save command, and displaying frames, respectively.
   - **Open-Closed Principle:** New functionalities (like different ways to process frames or save them) can be added by extending the respective classes without altering existing code.
   - **Liskov Substitution Principle:** Subtypes can be substituted without affecting functionality since the interface for processing frames remains consistent.
   - **Dependency Inversion Principle:** High-level modules (`FrameViewer`) do not depend on low-level modules; instead, they depend on abstractions (commands).

2. **GoF Design Patterns:**
   - **Factory Method:** The `VideoCaptureFactory` is used to create video capture objects without specifying the exact implementation.
   - **Command Pattern:** `FrameCaptureCommand` encapsulates the command to save the frame, allowing for flexible handling.
   - **Adapter:** Implicitly applied, as the `FrameViewer` class integrates the frame capture and processing logic.

3. **Environment Variables:**
   - Utilized `python-dotenv` to manage configurable parameters like the directory and name for saved frames.

### **.env Example:**
Create a `.env` file in the same directory as your script, containing:

```
FRAME_DIR=desired/path/to/store/frames
FRAME_NAME=person
```

