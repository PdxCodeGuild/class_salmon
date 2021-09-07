from django.contrib.auth.models import AbstractUser
from django.db import models

# class User(models.Model):
#     fname = models.CharField(max_length=50)
#     lname = models.CharField(max_length=50)
#     email = models.EmailField()
#     username = models.CharField(max_length=50)
#     wins = models.IntegerField()
#     losses = models.IntegerField()

class CustomUser(AbstractUser):

    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    user_image = models.ImageField()

    def __str__(self):
        return self.username
