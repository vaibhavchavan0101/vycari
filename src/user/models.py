from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .custom_user_manager import CustomUserManager

class User(AbstractUser):
    username = models.CharField(unique=True, max_length=50, blank=False)
    email = models.EmailField(unique=True, blank=False)
    bio= models.CharField(max_length=100)
    phone = models.CharField(max_length=13, unique=True, null=False, blank=False)
    password = models.CharField(max_length=200, null= False, blank= False)
    country= models.CharField(max_length=50)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ] 

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)  
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'gender', 'bio', 'phone', 'country']
    
    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Categories(models.Model):
    name= models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

class UserCategories(models.Model):
    user= models.ForeignKey('User', on_delete=models.CASCADE)
    category= models.ForeignKey('Categories', on_delete=models.CASCADE)
