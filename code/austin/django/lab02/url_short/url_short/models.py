from django.db import models
from django.conf import settings

# Create your models here.
class Shortener(models.Model):
    code = models.CharField(max_length=10,unique = True)
    url = models.URLField()

    def __str__(self):
        return self.url