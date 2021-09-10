from rest_framework import generics

from app_nfl import models
from app_sq
from .serializers import NFLSerializer

class ListTeams(generics.ListCreateAPIView):
    queryset = models.Team.objects.all()
    serializer_class = NFLSerializer


class DetailTeam(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Team.objects.all
    serializer_class = NFLSerializer
