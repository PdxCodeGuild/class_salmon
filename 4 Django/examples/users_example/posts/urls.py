from django.urls import path

from .views import detail, create

app_name = 'posts'
urlpatterns = [
    path('create', create, name='create'),
    path('<int:pk>', detail, name='detail'),
]