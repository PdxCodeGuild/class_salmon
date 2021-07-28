from django.urls import path
from . import views

app_name = 'posts_app' # for namespacing
urlpatterns = [
    path('', views.posts_app, name='posts_app')
]