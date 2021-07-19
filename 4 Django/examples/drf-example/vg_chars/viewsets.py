from rest_framework.viewsets import ModelViewSet

from vg_chars.models import Character, Franchise
from vg_chars.serializers import CharacterSerializer, FranchiseSerializer

class CharacterViewSet(ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filter_fields = {
        'first_appeared': ['gte', 'lt'],
        'franchise': ['exact'],
    }

class FranchiseViewSet(ModelViewSet):
    queryset = Franchise.objects.all()
    serializer_class = FranchiseSerializer
    filter_fields = ['developer']