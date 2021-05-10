from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, UserViewSet
# from .views import PostList, PostDetail, UserList, UserDetail

# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view()),
#     path('', PostList.as_view()),
#     path('user/', UserList.as_view()),
#     path('user/<int:pk>/', UserDetail.as_view()),
# ]

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls