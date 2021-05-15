from django.db import models
from django.urls import reverse
from datetime import timedelta

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', args=[str(self.id)])

    @property
    def created_updated_differ(self):
        return (self.updated - self.created) > timedelta(seconds=1)
