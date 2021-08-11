from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    wins = models.IntegerField()
    losses = models.IntegerField()
