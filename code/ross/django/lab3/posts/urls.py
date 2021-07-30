from django.urls import path
from django.contrib import admin
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('posts/new', views.CreateChirp.as_view(), name='chirp'),
]