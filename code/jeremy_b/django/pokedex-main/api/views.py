
from pokemon.models import Pokemon, Type
from .serializers import PokemonDetailSerializer,  TypeDetailSerializer, UserDetailSerializer
from rest_framework import viewsets, generics
from django.contrib.auth import get_user_model


# Create your views here.
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonDetailSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeDetailSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserDetailSerializer


class UserView(generics.RetrieveAPIView):
    serializer_class = UserDetailSerializer

    def get_object(self):
        return self.request.user