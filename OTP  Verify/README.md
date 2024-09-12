### Overview of Changes

1. **Single Responsibility Principle**: The code is segmented into multiple classes each handling a specific responsibility:
    - `OTPGenerator`: Responsible for OTP generation.
    - `EmailService`: Responsible for sending emails.
    - `OTPService`: Orchestrates OTP creation and sending.
    - `OTPVerifier`: Verifies the OTP input by the user.

2. **Open-Closed Principle**: The classes are designed to be open for extension (e.g., you can extend `EmailService` to support different email providers) but closed for modification.

3. **Liskov Substitution Principle**: The use of interfaces and abstract classes allows for subclasses to replace base classes without altering the operation of the program.

4. **Inversion of Control and Dependency Injection**: Dependencies are injected into classes, allowing for better management of dependencies and easier testing (mocking services, etc.). 

5. **Environment Variables**: The sensitive data, like SMTP credentials, are handled via environment variables.

### .env File Example

Create a `.env` file in the same directory as your script with the following content:

```
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_USERNAME=your-email@example.com
EMAIL_PASSWORD=your-email-password
```

#