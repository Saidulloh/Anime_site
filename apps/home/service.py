from django.core.mail import send_mail


def send(subject, message, from_email):
    send_mail(
        f'У вас новое сообщение от: {from_email} \n{subject}',
        message,
        'ssavutokhunov@gmail.com',
        ['ssavutokhunov@gmail.com'],
        fail_silently=False
    )