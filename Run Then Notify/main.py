import sys
from services.email_service import EmailService
from services.command_runner import CommandRunner

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py 'your_command_here'")
        sys.exit(1)

    command = sys.argv[1]

    # Initialize EmailService with environment variables
    email_service = EmailService(
        smtp_server=os.getenv("SMTP_SERVER"),
        smtp_port=int(os.getenv("SMTP_PORT")),
        sender_email=os.getenv("USER_EMAIL"),
        sender_password=os.getenv("USER_PASSWORD")
    )

    # Run command and notify
    command_runner = CommandRunner(email_service, os.getenv("USER_EMAIL"))
    command_runner.run_and_notify(command)
