import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file


class EmailService:
    def __init__(self, sender_email: str, sender_password: str):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.smtp_server = smtplib.SMTP(os.getenv('SMTP_SERVER'), int(os.getenv('SMTP_PORT')))
        self.smtp_server.starttls()
    
    def login(self):
        self.smtp_server.login(self.sender_email, self.sender_password)
    
    def send_email(self, message: MIMEMultipart):
        self.smtp_server.sendmail(self.sender_email, message['To'], message.as_string())
    
    def quit(self):
        self.smtp_server.quit()


class EmailBuilder:
    def __init__(self, subject: str, body: str, recipient: str):
        self.subject = subject
        self.body = body
        self.recipient = recipient

    def build_message(self) -> MIMEMultipart:
        message = MIMEMultipart()
        message['From'] = os.getenv('SENDER_EMAIL')
        message['To'] = self.recipient
        message['Subject'] = self.subject
        message.attach(MIMEText(self.body, 'plain'))
        return message


class AttachmentHandler:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def attach(self, message: MIMEMultipart):
        with open(self.file_path, 'rb') as attach_file:
            payload = MIMEBase('application', 'octate-stream')
            payload.set_payload(attach_file.read())
            encoders.encode_base64(payload)
            payload.add_header('Content-Disposition', 'attachment', filename=os.path.basename(self.file_path))
            message.attach(payload)


def main():
    subject = 'Sales Report 2021-- Team Sales'
    body = '''Hello, Admin

I am attaching The Sales Files With This Email.

This Year We Got a Wooping 200% Profit On Our Sales.

Regards,

Team Sales

xyz.com
'''
    
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    receiver_email = os.getenv('RECEIVER_EMAIL')
    attachment_path = os.getenv('ATTACHMENT')

    email_service = EmailService(sender_email, sender_password)
    email_service.login()

    email_builder = EmailBuilder(subject, body, receiver_email)
    message = email_builder.build_message()

    attachment_handler = AttachmentHandler(attachment_path)
    attachment_handler.attach(message)

    email_service.send_email(message)
    email_service.quit()

    print('Mail Sent')


if __name__ == '__main__':
    main()
