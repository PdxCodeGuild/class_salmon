from django.urls import path
from .views import SignUpView, UsersAppProfileView

app_name = 'users'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<str:username>/', UsersAppProfileView.as_view(), name='profile')
]