from django.urls import path

from . import views

app_name = 'users_app'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<str:username>/', views.UsersAppProfileView.as_view(), name='profile'),
]