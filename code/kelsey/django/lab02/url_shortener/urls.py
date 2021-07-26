from django.urls import path
from .views import home_view

appname = 'shortener'

urlpatterns = [
    path('', views.index, name='home'),
]
