from rest_framework import serializers
from pokemon.models import Pokemon, Type
from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', )
        model = CustomUser


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('type',)
        model = Type


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        types = serializers.SerializerMethodField('get_types')
        fields = (
            'name',
            'height',
            'weight',
            'image_front',
            'image_back',
            'caught_by',
            'number',
        )
        model = Pokemon


class PokemonDetailSerializer(serializers.ModelSerializer):
    type_name = TypeSerializer(read_only=True, many=True, source='types')
    users_caught = UserSerializer(read_only=True, many=True, source='caught_by')
    class Meta:
        fields =(
            'id',
            'name',
            'height',
            'weight',
            'image_front',
            'image_back',
            'caught_by',
            'number',
            'users_caught',
            'type_name',
        )
        model = Pokemon


class TypeDetailSerializer():
    pokemon_info = PokemonSerializer(read_only=True, many=True)
    class Meta:
        fields =(
            'id',
            'type',
            'pokemon',
            'pokemon_info',
        )

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'username',
            'date_joined',
            'caught',
        )
        model = CustomUser
