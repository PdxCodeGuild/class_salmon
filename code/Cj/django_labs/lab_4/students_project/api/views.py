from rest_framework import generics, viewsets
from django.contrib.auth import get_user_model

from students.models import Students
from.serializers import StudentSerializer


class ListStudents(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

class DetailStudents(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
