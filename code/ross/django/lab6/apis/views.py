from rest_framework import generics

from students import models
from students.models import Student
from .serializers import StudentSerializer

class ListStudent(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
    
class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer

class NameList(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        firstname = self.kwargs['firstname']
        return Student.objects.filter(firstname=firstname)

# from rest_framework import viewsets

# from students import models
# from .serializers import StudentSerializer


# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = models.Student.objects.all()
#     serializer_class = StudentSerializer