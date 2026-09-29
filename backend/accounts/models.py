from types import NoneType
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length = 30, unique = True)
    email = models.EmailField(unique = True)
    date_joined = models.DateTimeField(default=timezone.now())
    avatar_file = models.ImageField(null = True, blank = True)
    password = models.CharField(max_length = 128)

    def __str__(self):
        return self.username
