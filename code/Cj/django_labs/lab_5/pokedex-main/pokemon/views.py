from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Pokemon, Type

class PokemonListView(ListView):
    model = Pokemon
    template_name = 'home.html'

# class PokemonDetailView(DetailView):
#     model = Pokemon
#     template_name = 'pokemon_detail.html'

