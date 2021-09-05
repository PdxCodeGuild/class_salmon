from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=128)
    created = models.DateTimeField(default=timezone.now)




