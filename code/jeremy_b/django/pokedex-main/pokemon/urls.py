from .views import home_view
from django.urls import path, include

urlpatterns = [
    path('', home_view, name='home'),
]