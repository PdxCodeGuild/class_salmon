from rest_framework import serializers
from django.contrib.auth import get_user_model

from pokemon.models import Pokemon, Type, SoundEffect
from users.models import CustomUser


class NestedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = (
            'type',
            'type_tag',
        )

class NestedPokemonSerializer(serializers.ModelSerializer):
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
        )


class nestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields =(
            'username',
            'caught',
            
        )
        model = CustomUser

class PokemonSerializer(serializers.ModelSerializer):
    type_detail = NestedTypeSerializer(read_only=True, many=True, source='types')
    trainers = nestedUserSerializer(read_only=True, many=True, source='caught_by')
    class Meta:
        fields = (
            'id',
            'number',
            'name',
            'height',
            'weight',
            'image_front',
            'image_back',
            'caught_by',
            'trainers',
            'type_detail',
            'types',
            'gif',
            'cry',
        )
        model = Pokemon

class CaughtSerializer(serializers.ModelSerializer):
    type_detail = NestedTypeSerializer(read_only=True, many=True, source='types')

    class Meta:
        fields = (
            'id',
            'number',
            'name',
            'height',
            'weight',
            'image_front',
            'image_back',
            'type_detail',
            'types',
            'gif',
            'cry',
        )
        model = Pokemon

class TypeSerializer(serializers.ModelSerializer):
    pokemon_detail = NestedPokemonSerializer(read_only=True, many=True, source='pokemon')
    class Meta:
        fields = (
            'id',
            'type_tag',
            'type',
            'pokemon_detail',
        )
        model = Type

class SoundEffectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'media',
        )
        model = SoundEffect

class UserSerializer(serializers.ModelSerializer):
    caught_pokemon = CaughtSerializer(read_only=True, many=True, source='caught')
    class Meta:
        fields =(
            'id',
            'username',
            'caught',
            'caught_pokemon',
            
        )
        model = CustomUser