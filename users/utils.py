from django.contrib.auth import authenticate, get_user_model
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from rest_framework import serializers

from tasks_app.tasks import send_email_notification


def get_and_authenticate_user(email, password):
    user = authenticate(email=email, password=password)
    if user is None:
        raise serializers.ValidationError("Invalid username/password. Please try again!")
    return user


def create_user_account(email, password, first_name="",
                        last_name="", **extra_fields):
    user = get_user_model().objects.create_user(
        email=email, password=password, first_name=first_name,
        last_name=last_name, **extra_fields)
    return user


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    send_email_notification.delay(reset_password_token.user.email,
                                  'To reset your password: ' + "{}?token={}".format(
                                      instance.request.build_absolute_uri(
                                          reverse('password_reset:reset-password-confirm')),
                                      reset_password_token.key))
