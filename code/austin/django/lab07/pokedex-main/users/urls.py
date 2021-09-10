from django.urls import path
from .views import SignUpView, UserAppProfileView

app_name = 'users'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<str:username>/', UserAppProfileView.as_view(), name="profile")
]