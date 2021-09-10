from rest_framework import generics, viewsets
from django.contrib.auth import get_user_model

from pokemon.models import Pokemon
from .serializers import PokemonSerializer, TypeSerializer, UserSerializer
# from .permissions import IsAuthorOrReadOnly

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    # permission_classes = [IsAuthorOrReadOnly]

class TypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = TypeSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class CurrentPokemonView(generics.RetrieveAPIView):
    serializer_class = PokemonSerializer
    def get_object(self):
        return self.request.user

# class ListPokemon(generics.ListCreateAPIView):
#     queryset = models.Pokemon.objects.all()
#     serializer_class = PokemonSerializer

# class DetailPokemon(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Pokemon.objects.all()
#     serializer_class = PokemonSerializer

# class ListType(generics.ListCreateAPIView):
#     queryset = models.Type.objects.all()
#     serializer_class = TypeSerializer

# class DetailType(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Type.objects.all()
#     serializer_class = TypeSerializer