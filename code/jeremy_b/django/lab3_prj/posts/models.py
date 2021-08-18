from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    post_body = models.CharField(max_length=140)
    post_image = models.ImageField(upload_to='images/')
    post_author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post_created = models.DateTimeField(auto_now_add=True)
    post_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_body

    def absolute_url(self):
        return reverse('posts:detail', args=[self.id])

    class Meta:
        ordering = ['-post_created']