# Run then Notify

This is a python script that will run any terminal command on a system and once the command successfully runs, it will notify you via email of its time taken and the exit code.

This can be useful in case of long running commands.

Please enter your email and password when prompted. These values are _not_ stored anywhere and are only used for the SMTP connection.

> This system has a hardcoded gmail smtp server specified. In case of any other smtp server, please update the value in code.
>
> **Note**: You may have to enable `less secure app access` in your gmail account.
<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->


### 1. Directory Structure
You can implement the following structure for better organization:
```
project/
│
├── .env
├── main.py
└── services/
    ├── email_service.py
    ├── command_runner.py
```

### 2. .env File
Create a `.env` file for configuration like email, password, and SMTP details:
```env
USER_EMAIL=your_email@example.com
USER_PASSWORD=your_password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

### Summary of Changes
1. **SOLID Principles**:
   - **Single Responsibility Principle**: Each class handles one responsibility.
   - **Open-Closed Principle**: You can extend functionality (e.g., add a new email service) without changing existing code.
   - **Liskov Substitution Principle**: Substitutable classes guarantee the same behavior.
   - **Inversion of Control / Dependency Injection**: Dependencies are passed at initialization rather than hardcoded.
  
2. **Design Patterns Usage**:
   - **Facade**: The `EmailService` simplifies complex email sending operations.
   - **Command**: The `CommandRunner` encapsulates running commands and notifications.
