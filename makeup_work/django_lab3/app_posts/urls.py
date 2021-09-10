from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

app_name = "app_posts"
urlpatterns = [
    path('', PostListView.as_view(), name="postsHome"),
    path('post/<int:pk>/', PostDetailView.as_view(), name='postDetail'),
    path('post/new/', PostCreateView.as_view(), name="postCreate"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='postUpdate'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='postDelete'),
    path('about/', views.about, name="postsAbout"),

]