from users.models import CustomUser
from rest_framework import serializers
from django.contrib.auth import get_user_model
from pokemon import models

class NestedPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pokemon
        fields = ('id', 'name')

class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Type
        fields = ('id', 'type')

class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', )

class PokemonSerializer(serializers.ModelSerializer):
    type_detail = NestedTypeSerializer(read_only = True, many = True, source = 'types')
    caught_by_user = NestedUserSerializer(read_only = True, many  = True, source = 'caught_by')
    class Meta:
        model = models.Pokemon
        fields = ('id','name','type_detail', 'height', 'weight', 'image_front', 'image_back', 'caught_by_user')
        

class TypeSerializer(serializers.ModelSerializer):
    pokemon_detail = NestedPokemonSerializer(read_only = True, many = True, source = 'pokemon')
    class Meta:
        model = models.Type
        fields = ('id','type', 'pokemon', 'pokemon_detail')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','username','date_joined', 'caught')
        