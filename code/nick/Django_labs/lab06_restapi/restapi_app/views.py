from rest_framework import generics

from students.models import Students
from .serializers import StudentsSerializer

class StudentsView(generics.ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer