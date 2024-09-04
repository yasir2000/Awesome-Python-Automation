### Key Refactoring Points:

1. **Single Responsibility Principle**: Each class has a specific purpose; `SMTPConfig` handles SMTP configurations, while `EmailService` manages the email sending logic.

2. **Open/Closed Principle**: The `EmailService` class is open for extension (by adding more email methods) but closed for modification as it does not require changes when new types of email delivery methods are introduced.

3. **Liskov Substitution Principle**: Any subclass of `SMTPConfig` can replace it without changing the behavior of `EmailService`.

4. **Inversion of Control**: Dependencies are injected through the constructor, allowing flexibility and testing.

5. **Environment Variables**: All necessary variables are now retrieved from environment variables.

6. **Test Case**: A basic test case illustrates how to call the `send_email` method, allowing for mock implementations to prevent actual emails from being sent in tests.

This refactor enhances maintainability and testability while adhering to the specified requirements. 

Here's a sample `.env` file that you can use to configure the environment variables for the refactored email sending service:

```plaintext
# SMTP Configuration
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587

# Sender Information
SENDER_EMAIL=your-email@gmail.com
SENDER_NAME=Your Name
EMAIL_PASSWORD=your-email-password

# Email Defaults
EMAIL_SUBJECT=Good Morning
EMAIL_BODY=Good morning, hope you have a wonderful day

# Receiver Emails (comma-separated)
RECEIVER_EMAILS=receiver1-email@gmail.com,receiver2-email@gmail.com,receiver3-email@gmail.com
```

### Notes:
- Ensure you replace placeholders like `your-email@gmail.com` and `your-email-password` with actual values.
- Remember to keep your `.env` file secure and not to share it publicly, especially with sensitive information such as passwords. 
- You can load the variables from this file into your application using a library like `python-dotenv` or build support into your application if you are not already using a framework that handles it. 