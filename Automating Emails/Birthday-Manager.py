import csv
import smtplib
import ssl
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class EmailSender:
    def __init__(self, sender_address, sender_password):
        self.sender_address = sender_address
        self.sender_password = sender_password
        self.context = ssl.create_default_context()

    def send_email(self, recipient_email, message):
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=self.context) as server:
            server.login(self.sender_address, self.sender_password)
            server.sendmail(self.sender_address, recipient_email, message)

class BirthdayManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def read_birthdays(self):
        with open(self.csv_file, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            return [row for row in reader]

    def add_birthday(self, new_data):
        with open(self.csv_file, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(new_data)

    def remove_birthday(self, first_name):
        lines = []
        with open(self.csv_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] != first_name:  # Keep all except the one to remove
                    lines.append(row)

        with open(self.csv_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(lines)

class BirthdayEmailNotifier:
    def __init__(self, email_sender, birthday_manager):
        self.email_sender = email_sender
        self.birthday_manager = birthday_manager
        self.message_template = "Hi {fname},\n\nI wish you a very Happy Birthday.\n\nI hope you had a great day."

    def notify_birthdays(self):
        birthdays = self.birthday_manager.read_birthdays()
        for fname, lname, email, dob in birthdays:
            message = self.message_template.format(fname=fname)
            self.email_sender.send_email(email, message)

# Main execution flow
if __name__ == "__main__":
    sender_address = os.getenv("SENDER_ADDRESS")
    sender_password = os.getenv("SENDER_PASSWORD")

    email_sender = EmailSender(sender_address, sender_password)
    birthday_manager = BirthdayManager("birthday.csv")
    notifier = BirthdayEmailNotifier(email_sender, birthday_manager)

    notifier.notify_birthdays()

    choice = input("Do you wish to add or remove names from the csv file? (add/remove/exit): ").strip().lower()
    if choice == "add":
        new_data = input("Enter data as first name,lastname,email,date of birth: ").split(",")
        birthday_manager.add_birthday(new_data)
    elif choice == "remove":
        removal = input("Enter the first name of the person to be removed: ")
        birthday_manager.remove_birthday(removal)
