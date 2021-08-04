from django.urls import path
from django.contrib import admin
from . import views

app = 'url_short'

urlpatterns = [
    path('', views.index, name='index'),
    path('redirect/', views.redirect, name='redirect'),
]