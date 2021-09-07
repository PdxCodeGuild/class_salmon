from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import StudentViewSet

router = DefaultRouter()
router.register('student', StudentViewSet, basename='student')

urlpatterns = router.urls