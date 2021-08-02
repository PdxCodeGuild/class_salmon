from django.db import models
from django.urls import reverse

class Chirp(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    posted = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=128)

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse('chirps:detail', args=[self.id])

    class Meta:
        ordering = ['-posted']