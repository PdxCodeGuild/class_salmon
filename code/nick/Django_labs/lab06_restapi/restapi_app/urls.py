from django.urls import path
from .views import StudentsView

urlpatterns = [
    path('', StudentsView.as_view(), name='home')
]
