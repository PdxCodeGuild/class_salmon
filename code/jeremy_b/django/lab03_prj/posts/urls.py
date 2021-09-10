from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('add/', views.NewPost.as_view(), name='add_post')
]