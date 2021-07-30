from django.urls import path
from django.contrib import admin
from . import views
# from posts.views import home

app_name = 'posts'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('posts/new', views.CreateChirp.as_view(), name='chirp'),
    path('posts/user_feed', views.Home.as_view(), name='user_feed'),
]