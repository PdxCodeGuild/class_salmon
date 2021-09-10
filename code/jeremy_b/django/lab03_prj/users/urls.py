from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('signup', views.signup, name="signup"),
    url('login', LoginView.as_view(), name="login"),
    url('logout', LogoutView.as_view(), name="logout")
]