from django.urls import path
from . import views

app_name = "app_posts"
urlpatterns = [
    path('', views.home, name="posts-home"),
    path('about/', views.about, name="posts-about"),

]