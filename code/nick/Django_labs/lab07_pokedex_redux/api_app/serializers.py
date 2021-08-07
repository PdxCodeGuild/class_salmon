from pokemon.models import Pokemon, Type
from rest_framework import serializers
from django.contrib.auth import get_user_model

from pokemon.models import Pokemon

class NestedPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('id', 'number', 'name', 'height', 'weight', 'image_front', 'image_back', 'caught_by')

class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'type', 'pokemon')

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

class PokemonSerializer(serializers.ModelSerializer):
    username_detail = NestedUserSerializer(read_only=True, source='username')
    type_detail = NestedTypeSerializer(read_only=True, source='type')
    class Meta:
        model = Pokemon
        fields = ('id', 'number', 'name', 'height', 'weight', 'image_front', 'image_back', 'caught_by', 'username_detail', 'type_detail')

class TypeSerializer(serializers.ModelSerializer):
    pokemon_detail = NestedPokemonSerializer(read_only=True, many=True, source='pokemon_set')
    class Meta:
        model = Type
        fields = ('id', 'type', 'pokemon', 'pokemon_detail')

class UserSerializer(serializers.ModelSerializer):
    pokemon_detail = NestedPokemonSerializer(read_only=True, many=True, source='caught')
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'date_joined', 'caught', 'pokemon_detail')