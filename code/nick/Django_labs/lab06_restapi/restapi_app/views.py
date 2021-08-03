from rest_framework import generics, viewsets
from django.contrib.auth import get_user_model

from students_app.models import Students
from .serializers import StudentsSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [IsAuthorOrReadOnly]

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer