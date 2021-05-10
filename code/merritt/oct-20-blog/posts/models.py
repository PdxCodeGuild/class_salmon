from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    caption = models.CharField(max_length=500)
    photo = models.ImageField(upload_to="images/")

    def get_absolute_url(self):
        return reverse('instaface:detail', args=(self.id,))

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']