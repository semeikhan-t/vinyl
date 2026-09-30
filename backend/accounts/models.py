from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, UnicodeUsernameValidator


class User(AbstractUser):
    username = models.CharField(max_length = 30, unique = True)
    email = models.EmailField(unique = True)
    date_joined = models.DateTimeField(auto_now_add=True)
    avatar_file = models.ImageField(null = True, blank = True)
    password = models.CharField(max_length = 128)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']