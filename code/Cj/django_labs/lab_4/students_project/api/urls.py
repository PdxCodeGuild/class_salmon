from django.urls import path

from .views import ListStudents, DetailStudents, StudentsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', StudentsViewSet, basename='students')
urlpatterns = router.urls

# urlpatterns = [
#     path('', ListStudents.as_view()),
#     path('<int:pk>/', DetailStudents.as_view()),
# ]