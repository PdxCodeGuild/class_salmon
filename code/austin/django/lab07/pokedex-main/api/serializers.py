from rest_framework import serializers
from pokemon import models

class NestedPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pokemon
        fields = ('id', 'name')

class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Type
        fields = ('id', 'type')

class PokemonSerializer(serializers.ModelSerializer):
    type_detail = NestedTypeSerializer(read_only = True, many = True, source = 'types')
    class Meta:
        model = models.Pokemon
        fields = ('id','name','type_detail', 'height', 'weight', 'image_front', 'image_back', 'caught_by')
        

class TypeSerializer(serializers.ModelSerializer):
    pokemon_detail = NestedPokemonSerializer(read_only = True, many = True, source = 'pokemon')
    class Meta:
        model = models.Type
        fields = ('id','type', 'pokemon_detail')
        