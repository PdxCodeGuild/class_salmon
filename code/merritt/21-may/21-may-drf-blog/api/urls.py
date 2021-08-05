from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, UserViewSet, CurrentUserView

# from .views import PostList, PostDetail

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('users', UserViewSet, basename='users')

urlpatterns = router.urls + [
    path('currentuser/', CurrentUserView.as_view())
]

# urlpatterns = [
#     path('posts/<int:pk>/', PostDetail.as_view()),
#     path('posts/', PostList.as_view()),
# ]
