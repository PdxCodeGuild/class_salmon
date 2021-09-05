from django.urls import path
from .views import SignUpView, catch
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('catch/', views.catch, name='catch'),
]