### Explanation of Design Patterns and SOLID Principles Used

1. **Single Responsibility Principle (SRP)**: Each class has a single responsibility:
   - `CameraFactory` for camera creation.
   - `SelfieTaker` for handling the selfie-taking process.
   - `SelfieApp` for application control flow.

2. **Open/Closed Principle (OCP)**: The `CameraFactory` can be extended to create different types of cameras without modifying existing code. If you later want to add different camera sources, you can create subclasses of `CameraFactory`.

3. **Liskov Substitution Principle (LSP)**: Any new camera factory can replace `DefaultCameraFactory` without affecting the functionality of the `SelfieApp`.

4. **Dependency Inversion Principle (DIP)**: The `SelfieApp` depends on the abstract class `SelfieTaker`, not on concrete implementations, allowing for flexibility in changing the selfie taker.

5. **Design Patterns**:
   - **Factory Method**: `CameraFactory` abstracts the instantiation of the camera.
   - **Decorator (Not explicitly implemented here but can be extended)**: You could add functionality to `SelfieTaker` by wrapping it in decorators.
   - **Facade**: The `SelfieApp` provides a simple interface to the user, abstracting the detailed operations of taking selfies.

### Environment Variable Setup

Here is a sample `.env` file:

```
CAMERA_INDEX=0
IMAGE_DIR=./selfies
```
