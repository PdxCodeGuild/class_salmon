from pokemon.models import Pokemon
from django.shortcuts import render
from django.views.generic import ListView

from .models import Pokemon


# class PokemonListView(ListView):
#     model = Pokemon
#     template_name = 'home.html'

def Home(request):
    # pokemon = Pokemon.objects.all()
    return render(request, 'home.html')