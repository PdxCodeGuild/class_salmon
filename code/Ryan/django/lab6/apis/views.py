from rest_framework import generics, viewsets

from students import models
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer

# class ListCohort(generics.ListCreateAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = StudentSerializer
#
# class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = StudentSerializer
