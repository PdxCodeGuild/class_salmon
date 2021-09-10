from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=128)
    date_posted = models.DateTimeField(default=timezone.now)
