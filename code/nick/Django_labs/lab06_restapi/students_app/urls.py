
from django.urls import path

from .views import StudentsListView

urlpatterns = [
    path('', StudentsListView.as_view(), name='home'),
]