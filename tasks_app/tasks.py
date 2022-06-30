from celery import shared_task

from django.core.mail import send_mail
from todo_app.settings import EMAIL_HOST_USER


@shared_task
def send_email_notification(email, text):
    send_mail(subject='Notification!',
              message=text,
              from_email=EMAIL_HOST_USER,
              recipient_list=[email], fail_silently=False)
    return None

