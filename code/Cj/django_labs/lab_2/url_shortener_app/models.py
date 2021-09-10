from django.db import models

# Create your models here.
class URL(models.Model):
    short_url = models.CharField(max_length=200)
    full_url = models.CharField(max_length=200)
    date_created = models.DateTimeField()

    def __str__(self):
        return self.full_url
