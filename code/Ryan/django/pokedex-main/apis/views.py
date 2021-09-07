from rest_framework import generics

from pokemon import models
from .serializers import PokemonSerializer

class ListPokemon(generics.ListCreateAPIView):
    queryset = models.Pokemon.objects.all()
    serializer_class = PokemonSerializer

class DetailPokemon(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Pokemon.objects.all()
    serializer_class = PokemonSerializer
