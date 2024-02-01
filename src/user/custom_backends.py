from django.contrib.auth.backends import ModelBackend
from .models import User
from django.db.models import Q

class CustomBackend(ModelBackend):
    """
    Custom authentication backend for Django.
    This backend allows authentication using email, password, or username. It extends Django's
    built-in ModelBackend for authentication purposes.
    """

    def authenticate(self, email=None, password=None, username=None, **kwargs):
        try:
            user = User.objects.get(Q(email=username) | Q(phone=username) | Q(username=username))
        except User.DoesNotExist:
            return None
        if password is None:
            return None
        if self.user_can_authenticate(user) and user.check_password(password) :
            return user