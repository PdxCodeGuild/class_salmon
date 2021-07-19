from rest_framework.decorators import api_view
from rest_framework.response import Response

from vg_chars import models, serializers

@api_view(['GET', 'POST'])
def special_view(request):
    if request.method == 'GET':
        characters = models.Character.objects.all()
        json = serializers.CharacterSerializer(characters, many=True)
        return Response(json.data)
        
    elif request.method == 'POST':
        character = serializers.CharacterSerializer(data=request.data)
        if character.is_valid():
            character.save()
            return Response(character.data)
        else:
            return Response(character.errors, status=400)