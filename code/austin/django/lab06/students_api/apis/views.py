from django.db.models.query import QuerySet
from rest_framework import generics, viewsets
""" from django.contrib.auth import get_user_model """

from students.models import Student
from .serializers import StudentSerializer




# Create your views here.

""" class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer """

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer