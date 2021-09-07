from django.forms import ModelForm
from django import forms

from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'image')