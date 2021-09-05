from rest_framework import serializers
from django.contrib.auth import get_user_model

from pokemon.models import Pokemon, Type
from users.models import CustomUser

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('type',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('pokemon_caught',)

class UserCaughtSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username',)

class PokemonSerializer(serializers.ModelSerializer):
    types = TypeSerializer(many=True, read_only=True)
    caught_by_users = UserCaughtSerializer(many=True, read_only=True)
    class Meta:
        model = Pokemon
        fields = ('number', 'name',  'types', 'height', 'weight', 'image_front', 'image_back', 'caught_by_users',)


# class NestedTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ('type', 'pokemon',)

# class NestedPokemonSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Pokemon
#         fields = ('number', 'name', 'height', 'weight', 'image_front', 'image_back', 'caught_by',)