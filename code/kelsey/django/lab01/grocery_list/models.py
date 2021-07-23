from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    text = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)
    # completed = 
    author = models.ForeignKey(User, on_delete=models.CASCADE)