from django.urls import path
# from .views import PostList, PostDetail
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, UserViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, base_name='posts')
router.register('users', UserViewSet, base_name='users')

urlpatterns = router.urls

# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view()),
#     path('', PostList.as_view()),
# ]