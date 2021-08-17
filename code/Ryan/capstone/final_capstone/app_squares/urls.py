from django.urls import path
from . import views

app_name = "square"
urlpatterns = [
    path("", views.CreateSquare, name="square-home"),
    path("<int:pk>/", views.index, name="square-id"),
    path("new/", views.CreateSquare, name="square-new")
]
