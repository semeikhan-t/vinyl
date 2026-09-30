from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length = 30)
    bio = models.CharField(max_length = 300)
    cover_file = models.ImageField(blank = True)

    class Meta:
        ordering = ['name']
