from rest_framework import serializers
from .models import *
from users.models import *
from pokemon.models import *
from django.contrib.auth import get_user_model

class NestedPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ("id", "number", "name", "height", "weight", "image_front", "image_back", "caught_by", )

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username")

class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ("id", "type",)

class PokemonSerializer(serializers.ModelSerializer):
    user_detail = NestedUserSerializer(read_only=True, source="pokemon")
    type_detail = NestedTypeSerializer(read_only=True, many=True, source="types")
    class Meta:
        model = Pokemon
        fields = ("id", "number", "name", "height", "weight", "image_front", "image_back", "caught_by", "types", "user_detail", "type_detail")

class UserSerializer(serializers.ModelSerializer):
    pokemon_detail = NestedPokemonSerializer(read_only=True, many=True)
    class Meta:
        model = get_user_model()
        fields = ("id", "username",)

class TypeSerializer(serializers.ModelSerializer):
    type_detail = NestedPokemonSerializer(read_only=True, many=True, source="types")
    class Meta:
        model = Type
        fields = ("id", "pokemon", "types",)
