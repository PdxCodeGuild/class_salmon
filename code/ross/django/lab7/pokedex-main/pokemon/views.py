from django.shortcuts import render
from .models import Pokemon
from django.shortcuts import get_object_or_404

# def catch(request, pk):
#     pokemon = get_object_or_404(Pokemon, pk=pk)
#     pokemon.caught_by = username
#     pokemon.save()
#     return HttpResponseRedirect(reverse('pokemon:home'))
