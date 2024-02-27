from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """Define a model manager for custom User model."""

    def create_user(self, username, email, phone, password, **extra_fields):
        email = self.normalize_email(email)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', False)
        user = self.model(email=email, username=username,
                          phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser permission.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active permisson.')
        return self.create_user(username, email, phone, password, **extra_fields)
