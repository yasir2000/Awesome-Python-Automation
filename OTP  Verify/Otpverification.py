import os
import random
import smtplib
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class OTPGenerator:
    """This class is responsible for generating OTPs."""
    def __init__(self, length=6):
        self.length = length
        self.digits = "0123456789"

    def generate_otp(self):
        return ''.join(random.choices(self.digits, k=self.length))

class EmailService:
    """This class is responsible for sending emails."""
    def __init__(self, smtp_server, smtp_port, username, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient_email, message):
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.username, self.password)
            server.sendmail(self.username, recipient_email, message)

class OTPService:
    """This class orchestrates OTP generation and sending."""
    def __init__(self, otp_generator: OTPGenerator, email_service: EmailService):
        self.otp_generator = otp_generator
        self.email_service = email_service
        self.otp = ""

    def create_and_send_otp(self, recipient_email):
        self.otp = self.otp_generator.generate_otp() + " is your OTP"
        self.email_service.send_email(recipient_email, self.otp)
        return self.otp

class OTPVerifier:
    """This class is responsible for verifying the OTP."""
    @staticmethod
    def verify(otp_input, generated_otp):
        return otp_input == generated_otp.split()[0]

def main():
    # Dependency Injection via Environment Variables
    smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    username = os.getenv("EMAIL_USERNAME")
    password = os.getenv("EMAIL_PASSWORD")

    otp_generator = OTPGenerator()
    email_service = EmailService(smtp_server, smtp_port, username, password)
    otp_service = OTPService(otp_generator, email_service)

    recipient_email = input("Enter your email: ")
    generated_otp = otp_service.create_and_send_otp(recipient_email)
    user_input = input("Enter Your OTP >>: ")
    
    if OTPVerifier.verify(user_input, generated_otp):
        print("Verified")
    else:
        print("Please Check your OTP again")

if __name__ == "__main__":
    main()
