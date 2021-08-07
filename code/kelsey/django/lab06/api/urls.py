from django.urls import path

from .views import StudentAPIView

urlpatterns = [
    path('', StudentAPIView.as_view()),
]
