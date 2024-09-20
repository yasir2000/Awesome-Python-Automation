### Explanation of Refactor

1. **SOLID Principles**:
   - **Single Responsibility Principle**: The `Server` class is in charge of socket management and client handling. Each method has a specific task—`start` manages the listening state while `handle_client` manages communication with the client.
   - **Open-Closed Principle**: The server can be extended with more methods (like logging, handling different types of protocols) without modifying existing code.
   - **Liskov Substitution Principle**: If you implement additional server types (say, for different protocols), they can inherit from this base class without breaking the functionality.
   - **Inversion of Control**: The IP and port are set externally via environment variables rather than hardcoded in the class.
   - **Dependency Injection**: The `Server` class receives its configurations (IP and port) via constructor parameters.

2. **GoF Design Patterns**:
   - **Facade Pattern**: The `Server` class serves as a facade that encapsulates the complexity of socket management and client handling, providing a clear interface to the user.
   - **Single Responsibility and Command Pattern**: The `handle_client` method encapsulates the command of handling messages, making it easier to modify the behavior of message handling.

3. **Environment Variables**: 
   - Use a `.env` file to specify the listening IP and port, enhancing flexibility without modifying the code.
  
### Step 4: Create the `.env` File

Create a file named `.env` in the same directory as the script, containing:

```
IP=0.0.0.0
PORT=3000
```

