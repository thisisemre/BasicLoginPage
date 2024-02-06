from os import environ
import smtplib, ssl

smtp_server = environ.get('SMTP_SERVER')
port = environ.get('MAIL_PORT')  # For starttls
sender_email = environ.get('MAIL_USERNAME')
password = environ.get('MAIL_PASSWORD')

context = ssl.create_default_context()


def send_mail(receiver, message):
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver, message)


def send_reset_password_mail(receiver, reset_url):
    message = f"""Subject: Reset your password

    Your reset link is {reset_url}.
    The link is going to expire in 5 min."""
    send_mail(receiver, message)
