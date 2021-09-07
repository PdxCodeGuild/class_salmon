from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('signup/',
         views.SignUpView.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('profile', views.user_profile, name='user_profile'),
]
