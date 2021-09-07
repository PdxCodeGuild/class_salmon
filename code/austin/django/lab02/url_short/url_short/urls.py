from django.urls import path
from url_short import views

app_name = 'url_short'

urlpatterns = [
    path('', views.index, name='index'),
    path('redirect/', views.redirect, name='redirect'),
]
