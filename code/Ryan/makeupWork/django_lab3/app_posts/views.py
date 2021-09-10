from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "app_posts/home.html", context)

def about(request):
    return render(request, "app_posts/about.html", {"title": "About"})

