from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('profile/', views.profile, name='profile')
]