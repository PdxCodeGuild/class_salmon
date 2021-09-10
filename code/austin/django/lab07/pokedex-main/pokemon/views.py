
from pokemon.models import Pokemon
from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.reverse import reverse_lazy, reverse

from .models import Pokemon


def Home(request):
    return render(request, 'home.html')

