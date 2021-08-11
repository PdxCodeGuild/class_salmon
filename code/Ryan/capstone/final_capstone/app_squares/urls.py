from django.urls import path
from . import views

app_name = "square"
urlpatterns = [
    path("", views.square, name="square-home")
    path("square/<int:pk>", views.square, name="square-id")
]
