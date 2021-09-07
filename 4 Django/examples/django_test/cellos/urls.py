from django.urls import path
from django.shortcuts import reverse
from . import views

app_name = 'cellos'
urlpatterns = [
    path('', views.cellos, name='list'),
    path('<int:id>', views.detail, name='detail'),
    path('random', views.random, name='random')
]