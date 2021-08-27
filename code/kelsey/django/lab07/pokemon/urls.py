from . import views
from django.urls import path, include
from django.views.generic import TemplateView

app_name = "pokemon"

urlpatterns = [
    path(''),
]