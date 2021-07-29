from django.urls import path
from . import views

app_name = "app_shortURL"
urlpatterns = [
    path('', views.index, name="index"),
    path('input/', views.InputURL, name="input"),
    path('redirect/', views.RedirectURL, name="redirect")
]
