from django.db import models
from django.conf import settings
from django.utils import timezone

class Shortener(models.Model):
    url = models.URLField(null=True)
    code = models.CharField(max_length=6, null=True)

    def __str__(self):
        return self.url