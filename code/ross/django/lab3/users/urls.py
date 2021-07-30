from django.urls import path
from django.contrib import admin
from django.urls import include
from django.contrib.auth.views import LoginView
from . import views
from users.views import signup_view, home_view, login_view, logout_view #, user_profile

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='login'),
    path('home', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    # path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # path('<str:username>/', views.user_profile, name='profile'),
    path('<str:username>/', views.UserProfileView.as_view(), name='profile'),
]