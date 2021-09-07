from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostView.as_view(), name='index'),
    path('post/detail/<int:pk>', views.PostDetailView.as_view(), name='detail'),
    path('post/create/', views.CreatePost.as_view(), name='new'),
    path('post/<int:pk>/edit/', views.EditPost.as_view(), name='edit'),
    path('post/<int:pk>/delete/', views.DeletePost.as_view(), name='delete'),
]
