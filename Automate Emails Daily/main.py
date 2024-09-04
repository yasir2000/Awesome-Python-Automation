import os
import smtplib
import ssl
from email.message import EmailMessage
from email.utils import formataddr
from typing import List

# Strategy for SMTP Configuration
class SMTPConfig:
    def __init__(self, server: str, port: int):
        self.server = server
        self.port = port

    def create_connection(self):
        ssl_context = ssl.create_default_context()
        connection = smtplib.SMTP(self.server, self.port)
        connection.starttls(context=ssl_context)
        return connection

# Email Service
class EmailService:
    def __init__(self, smtp_config: SMTPConfig):
        self.smtp_config = smtp_config

    def send_email(self, sender_email: str, sender_name: str, password: str,
                   receiver_emails: List[str], email_body: str, email_subject: str = "No Subject") -> None:
        
        msg = EmailMessage()
        msg["Subject"] = email_subject
        msg["From"] = formataddr((sender_name, sender_email))
        msg["BCC"] = sender_email
        msg.set_content(email_body)

        try:
            print("Connecting to Server...")
            with self.smtp_config.create_connection() as server:
                server.login(sender_email, password)
                print("Connected to server!")
                for receiver in receiver_emails:
                    msg["To"] = receiver
                    print(f"Sending email to: {receiver}")
                    server.sendmail(sender_email, receiver, msg.as_string())
                    print(f"... Successfully sent to: {receiver}")
        except Exception as e:
            print(f"ERROR: {e}")

# Environment Variables
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SENDER_EMAIL = os.getenv("SENDER_EMAIL", "your-email@gmail.com")
SENDER_NAME = os.getenv("SENDER_NAME", "your name")
PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_SUBJECT = os.getenv("EMAIL_SUBJECT", "Good Morning")
EMAIL_BODY = os.getenv("EMAIL_BODY", "Good morning, hope you have a wonderful day")
RECEIVER_EMAILS = os.getenv("RECEIVER_EMAILS", "receiver1-email@gmail.com,receiver2-email@gmail.com,receiver3-email@gmail.com").split(',')

# Execute the Email Sending Process
if __name__ == "__main__":
    smtp_config = SMTPConfig(SMTP_SERVER, SMTP_PORT)
    email_service = EmailService(smtp_config)

    email_service.send_email(SENDER_EMAIL, SENDER_NAME, PASSWORD, RECEIVER_EMAILS, EMAIL_BODY, EMAIL_SUBJECT)

# Test Case (For demonstration purposes)
def test_email_service():
    smtp_config = SMTPConfig("smtp.test.com", 587)  # Mock SMTP
    email_service = EmailService(smtp_config)

    # Mocking the send_email method to avoid sending an actual email during the test
    try:
        email_service.send_email("test@example.com", "Test User", "password", ["receiver@test.com"], "Test Body", "Test Subject")
        print("Test case executed successfully.")
    except Exception as e:
        print("Test case failed:", e)

# Uncomment to run test case
# test_email_service()
