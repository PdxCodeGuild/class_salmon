from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class url_short(models.Model):
    code = CharField(max_length=10,unique = True, blank = True)
    url = models
    date_created = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return f'{self.short_url} to {self.long_url}'