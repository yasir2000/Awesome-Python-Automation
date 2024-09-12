Email Sender Script Documentation

This Python script sends an email with an attachment using the smtplib library. It is designed to send a sales report email with a specific body and a file attachment. Below are the details and usage of the script:

Email Content:

    The email's body contains a simple message with a sales report for the year.
    The sender's email address and password should be specified in the script.
    The recipient's email address should also be provided in the script.


Code Explanation:

    The script uses the smtplib library to send emails.
    It constructs the email message with a subject, sender, recipient, and body text.
    It attaches the 'temp.txt' file to the email.
    It connects to the Gmail SMTP server, enables a secure connection, and logs in using the sender's credentials.
    The email message is converted to a string, sent, and the connection to the SMTP server is closed.
    A message, "Mail Sent," is printed to indicate that the email has been sent.

Please note that this script is set up for Gmail's SMTP server by default. If you are using a different email service, you may need to adjust the SMTP server details accordingly.

Ensure that you have allowed less secure apps to access your Gmail account or use an application-specific password for sending emails via Gmail

<!-- Updated README links and corrected typos -->
<!-- Updated README links and corrected typos -->


### Refactored Code

First, we need to create a `.env` file to store sensitive variables:

```plaintext
# .env file
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_password
RECEIVER_EMAIL=receiver_email@example.com
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
ATTACHMENT=path/to/temp.txt
```


### Explanation

1. **SOLID Principles**:
   - **Single Responsibility Principle**: Classes are responsible for only one aspect (sending emails, building messages, handling attachments).
   - **Open-Close Principle**: Classes can be extended without modifying existing code (you can add new methods or classes for different types of emails).
   - **Liskov Substitution Principle**: Any subclass can replace its superclass (if you create subclasses for `EmailService` for different providers).
   - **Inversion of Control & Dependency Injection**: `EmailService` operates with the sender email and password passed to it, promoting the use of dependency injection.

2. **GoF Design Patterns**:
   - **Builder**: Used to construct the email message.
   - **Composite**: An abstract representation of attachments. This can be expanded to support multiple attachments easily.
   - **Facade**: `EmailService` serves as a facade for email sending functionality.
   - **Prototype**: The attachment could implement a cloning mechanism if multiple attachments are derived from a template.

