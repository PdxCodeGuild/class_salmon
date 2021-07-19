from rest_framework import serializers

from vg_chars.models import Character, Franchise

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'

class FranchiseSerializer(serializers.ModelSerializer):
    characters = CharacterSerializer(many=True)
    class Meta:
        model = Franchise
        fields = '__all__'
