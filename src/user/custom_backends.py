from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework import status

class CustomBackend(ModelBackend):
    """
    Custom authentication backend for Django.
    This backend allows authentication using email, password, or username. It extends Django's 
    built-in ModelBackend for authentication purposes.
    """

    def authenticate(self, email=None, password=None, username=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(Q(email=username) | Q(phone=username) | Q(username=username))
        except User.DoesNotExist:
            return None
        if password is None:
            return None
        if user and user.check_password(password):
            return user