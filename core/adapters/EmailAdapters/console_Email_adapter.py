from core.ports.email_port import EmailPort
# from django.core.mail import send_mail

class ConsoleEmailAdapter(EmailPort):
    def send_email(self, subject: str, message: str, from_email: str, recipient_list: list):
        print(f"Sending email with subject: {subject}")
        # send_mail(subject, message, from_email, recipient_list) c