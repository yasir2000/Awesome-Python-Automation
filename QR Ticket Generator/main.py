import pandas as pd
import qrcode
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from fpdf import FPDF

class QRCodeGenerator:
    def generate(self, full_name: str, registration_number: str, unique_id: str, event_name: str) -> str:
        # Generate and save QR code
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(unique_id)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        qrcode_dir = f"{registration_number}.png"
        img.save(qrcode_dir)
        return qrcode_dir

class PDFGenerator:
    def generate(self, event_name: str, full_name: str, role: str, payment_status: str,
                 unique_id: str, qrcode_dir: str, registration_number: str) -> str:
        pdf = FPDF(format='A5', orientation='L')
        pdf.add_page()
        self._add_content(pdf, event_name, full_name, role, payment_status, unique_id, qrcode_dir)
        pdf_dir = f"{registration_number}.pdf"
        pdf.output(pdf_dir)
        return pdf_dir

    def _add_content(self, pdf, event_name, full_name, role, payment_status, unique_id, qrcode_dir):
        # Add heading, attendee name, etc.
        # Similar implementation as in the original code.

class EmailSender:
    def __init__(self, gmail_user, gmail_password):
        self.gmail_user = gmail_user
        self.gmail_password = gmail_password

    def send(self, email: str, full_name: str, event_name: str, pdf_dir: str):
        msg = MIMEMultipart()
        msg['From'] = self.gmail_user
        msg['To'] = email
        msg['Subject'] = 'Event Ticket'
        text = MIMEText(f"Hey {full_name},\n PFA of your event {event_name} Ticket")
        msg.attach(text)

        with open(pdf_dir, 'rb') as f:
            pdf = MIMEApplication(f.read(), _subtype='pdf')
            pdf.add_header('Content-Disposition', 'attachment', filename=os.path.basename(pdf_dir))
            msg.attach(pdf)

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(self.gmail_user, self.gmail_password)
            server.send_message(msg)

class DataManager:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_confirmed_payments(self):
        df = pd.read_excel(self.file_path)
        return df[df['payment status'] == 'captured']

def start_entry_process():
    data_manager = DataManager("InsertDataHERE.xlsx")
    email_sender = EmailSender('your_email@gmail.com', 'your_password')
    qr_code_generator = QRCodeGenerator()
    pdf_generator = PDFGenerator()

    confirmed_payments = data_manager.get_confirmed_payments()

    for index, row in confirmed_payments.iterrows():
        full_name = row['full_name'].upper()
        registration_number = row['registration_number'].upper()
        unique_id = row['order_id']
        event_name = row['payment button title']
        email = row['email']

        try:
            qrcode_path = qr_code_generator.generate(full_name, registration_number, unique_id, event_name)
            pdf_path = pdf_generator.generate(event_name, full_name, "ATTENDEE", "PAID", unique_id, qrcode_path, registration_number)
            email_sender.send(email, full_name, event_name, pdf_path)
        except Exception as e:
            print(f"Error processing {registration_number} - {full_name}: {e}")

if __name__ == '__main__':
    start_entry_process()
