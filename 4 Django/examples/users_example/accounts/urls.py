from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, user_profile

app_name = 'accounts'

# The manual way
# from .views import sign_in, register, sign_out
# urlpatterns = [
#     path('sign_in', sign_in, name='sign_in'),
#     path('sign_out', sign_out, name='sign_out'),
#     path('register', register, name='register'),
# ]

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', user_profile, name='profile')
]