from django.db import models
from django.conf import settings
from django.utils import timezone
from django import forms

class User(models.Model):
    username = models.CharField(max_length=16)
    password = forms.CharField(widget=forms.PasswordInput())

    def __str__(self):
        return self.contents