from rest_framework import serializers
from django.contrib.auth import get_user_model

from pokemon.models import Pokemon, Type

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('type',)

class PokemonSerializer(serializers.ModelSerializer):
    types = TypeSerializer(many=True, read_only=True)
    class Meta:
        model = Pokemon
        fields = ('number', 'name',  'types', 'height', 'weight', 'image_front', 'image_back', 'caught_by',)

# class NestedTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ('type', 'pokemon',)

# class NestedPokemonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Pokemon
#         fields = ('number', 'name', 'height', 'weight', 'image_front', 'image_back', 'caught_by',)