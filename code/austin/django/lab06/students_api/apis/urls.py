from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import StudentDetail, StudentList
""" from .views import StudentViewSet

router = DefaultRouter()
router.register('students', StudentViewSet, basename='students')

urlpatterns = router.urls """

urlpatterns = [
    path('students/<int:pk>/',StudentDetail.as_view()),
    path('students/', StudentList.as_view()),
]