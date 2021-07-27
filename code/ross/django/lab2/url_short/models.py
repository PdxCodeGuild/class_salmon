from django.db import models
from django.conf import settings
from django.utils import timezone

class Shortener(models.Model):
    url = models.CharField(max_length=200)
    code = models.CharField(max_length=6)

    def __str__(self):
        return self.url