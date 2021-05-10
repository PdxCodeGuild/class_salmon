from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.UserListView.as_view(), name='user_list'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<str:username>/', views.PostList.as_view(), name='post_list'),
]
