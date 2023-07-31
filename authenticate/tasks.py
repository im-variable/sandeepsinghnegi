# from time import sleep
from django.core.mail import send_mail
from celery import shared_task

@shared_task
def send_email_task(username, email_from, email_to):
    """Sends an email when the user registered."""
    subject = 'welcome to sandeepsinghnegi.in world'
    message = f'Hi {username}, thank you for registering in sandeepsinghnegi.in.'
    recipient_list = [email_to, ]
    res = send_mail( subject, message, email_from, recipient_list , fail_silently=False, )
    print('res' , res)
