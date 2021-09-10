from users.models import CustomUser
from rest_framework import serializers
from django.contrib.auth import get_user_model

from pokemon.models import Pokemon, Type


class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('type',)
class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', )

class NestedPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = (
            'number', 
            'name', 
            'height', 
            'weight', 
            'image_front', 
            'image_back', 
            'caught_by', 
            )
            
class PokemonSerializer(serializers.ModelSerializer):
    type_detail = NestedTypeSerializer(read_only=True, many=True, source='types')
    caught_by_users = NestedUserSerializer(read_only=True, many=True, source='caught_by')
    class Meta:
        model = Pokemon
        fields = (
            'id',
            'number', 
            'name', 
            'height', 
            'weight', 
            'image_front', 
            'image_back', 
            'caught_by', 
            'caught_by_users',
            'types',
            'type_detail',
            )  

class TypeSerializer(serializers.ModelSerializer):
    pokemon_detail = NestedPokemonSerializer(read_only=True, many=True, source='pokemon')
    class Meta:
        model = Type
        fields = ('id', 'type', 'pokemon', 'pokemon_detail')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'date_joined', 'caught')

    