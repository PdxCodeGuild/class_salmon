from django.db import models


# Create your models here.
class Shortener(models.Model):
    code = models.CharField(max_length=10,unique = True, null=True)
    url = models.URLField(null=True)

    def __str__(self):
        return self.url