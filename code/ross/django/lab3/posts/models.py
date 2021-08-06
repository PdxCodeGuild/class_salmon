from django.db import models
from django.forms import ModelForm
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    contents = models.CharField(max_length=70)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    time_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contents

    def get_absolute_url(self):
        return reverse("posts:home")
        # , kwargs={"pk": self.pk}

    # class Meta:
    #     ordering = ['-created']
    