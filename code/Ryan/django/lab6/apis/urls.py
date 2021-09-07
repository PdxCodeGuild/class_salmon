from django.urls import path
from .views import  StudentViewSet #ListCohort, DetailStudent,
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", StudentViewSet, basename = "students")

urlpatterns = router.urls

# urlpatterns = [
#     path("", ListCohort.as_view()),
#     path("<int:pk>/", DetailStudent.as_view())
#     ]
