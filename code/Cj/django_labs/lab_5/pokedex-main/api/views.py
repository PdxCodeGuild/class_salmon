from rest_framework import generics, viewsets
from django.contrib.auth import get_user_model

from pokemon.models import Pokemon, Type, SoundEffect
from users.models import CustomUser
from .serializers import PokemonSerializer, TypeSerializer, SoundEffectSerializer, UserSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class SoundEffectViewSet(viewsets.ModelViewSet):
    queryset = SoundEffect.objects.all()
    serializer_class = SoundEffectSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user