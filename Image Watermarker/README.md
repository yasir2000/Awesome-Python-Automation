
### Key Changes Made:

1. **Single Responsibility Principle (SRP)**: Each class has a distinct responsibility. `WatermarkConfig` handles configuration, `ImageProcessor` manages individual image processing, and `WatermarkBatchProcessor` handles the batch process.

2. **Open/Closed Principle (OCP)**: The design allows for easy extension. You can introduce more features by adding classes without modifying existing code.

3. **Liskov Substitution Principle (LSP)**: Subclasses can be used seamlessly, adhering to type expectations. The design encourages classes that adhere to the expectations set by their interfaces.

4. **Inversion of Control (IoC)**: The use of a configuration class allows the system to be flexible. Dependencies are injected via the constructor.

5. **Dependency Injection**: Dependencies like folder paths and watermark images are managed through environment variables, promoting decoupling.

6. **GoF Design Patterns**:
   - **Singleton**: `WatermarkConfig` ensures a single instance managing configuration.
   - **Facade**: `WatermarkBatchProcessor` simplifies the batch processing interface.
   - **Command**: Encapsulated actions like applying watermarking in the `ImageProcessor`.

### Environment Variables:
Ensure you define the `.env` file with the required variables as shown in the comments.

