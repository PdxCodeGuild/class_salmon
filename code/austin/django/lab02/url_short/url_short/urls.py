from django.urls import path
from . import views
from django.lab02.url_short import url_short

app_name = url_short
urlpatterns = [
    path('', views.index, name='index')
]
