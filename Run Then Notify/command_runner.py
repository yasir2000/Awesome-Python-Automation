import subprocess
import time
import socket

class CommandRunner:
    def __init__(self, email_service, user_email):
        self.email_service = email_service
        self.user_email = user_email

    def run_and_notify(self, command):
        start_time = time.time()
        completed_process = subprocess.run(command, text=True, shell=True,
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE)

        end_time = time.time()
        execution_time = end_time - start_time

        subject = '[Run completed] Your command finished execution'
        message = (f"Command '{command}' completed\n"
                   f"\twith exit code {completed_process.returncode}\n"
                   f"\tin {execution_time:.2f} seconds\n"
                   f"This is an automated message sent from your device {socket.gethostname()}")

        self.email_service.send_email(subject, message, self.user_email)
