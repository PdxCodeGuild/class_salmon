from django.db import models
from django.contrib import admin
from django.urls import path, include
# Create your models here.


class Post(models.Model):
    item_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        'auth.user', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.item_text
