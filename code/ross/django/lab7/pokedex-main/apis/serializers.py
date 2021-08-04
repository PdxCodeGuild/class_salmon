from rest_framework import serializers
from django.contrib.auth import get_user_model

from pokemon.models import Pokemon, Type

class NestedPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('number', 'name', 'height', 'weight', 'image_front', 'image_back', 'caught_by',)

class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('type', 'pokemon',)

class PokemonSerializer(serializers.ModelSerializer):
    pokemon_detail = NestedTypeSerializer(read_only=True, source='name')
    class Meta:
        model = Pokemon
        fields = ('number', 'name', 'height', 'weight', 'image_front', 'image_back', 'caught_by', 'pokemon_detail',)

class TypeSerializer(serializers.ModelSerializer):
    type_detail = NestedPokemonSerializer(read_only=True, many=True, source='type_set')
    class Meta:
        model = get_user_model()
        fields = ('type', 'type_set', 'type_detail',)