from django.urls import path

app_name = 'users'
from . import views

urlpatterns = [
    path('signup/', views.Signup.as_view(), name='signup'),
    path('<str:username>', views.UserProfile.as_view(), name='profile'),
]

