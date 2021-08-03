from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import StudentsViewSet, UserViewSet

router = DefaultRouter()
router.register('students', StudentsViewSet, basename='students')
router.register('users', UserViewSet, basename='users')

urlpatterns = router.urls