from django.urls import path

from .views import StudentListView

app_name = 'students'
urlpatterns = [
    path('', StudentListView.as_view(), name='home')
]