from django.db import models
from django.utils.duration import datetime

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 30, unique = True)
    email = models.EmailField(unique = True)
    date_joined = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.username
