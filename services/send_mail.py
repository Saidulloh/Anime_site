from .keys import *
from email.mime.text import MIMEText
import smtplib


def send_email(name, sender_email, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    message = f'Вам отправили сообщение: \n{message} \nUser name is {name} \nUser email {sender_email}'

    try:
        server.login(to, password)
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = to
        server.sendmail(to, to, msg.as_string())
        print('отправлено')
    except Exception as ex:
        return f'{ex}\nCheck your login or password!'
        