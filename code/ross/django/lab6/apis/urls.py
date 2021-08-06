from django.urls import path, re_path

from .views import ListStudent, DetailStudent, NameList

urlpatterns = [
    path('', ListStudent.as_view()),
    path('<int:pk>/', DetailStudent.as_view()),
    re_path('^students/(?P<firstname>.+)/$', NameList.as_view()),
]

# from django.urls import path

# from .views import StudentViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('', StudentViewSet, basename='students')
# urlpatterns = router.urls