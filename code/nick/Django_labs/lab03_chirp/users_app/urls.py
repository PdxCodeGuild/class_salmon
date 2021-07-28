from django.urls import path
from . import views

app_name = 'users_app' # for namespacing
urlpatterns = [
    path('', views.users_app, name='users_app')
]