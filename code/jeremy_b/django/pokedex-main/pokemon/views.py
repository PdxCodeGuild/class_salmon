from django.shortcuts import render
from .models import Pokemon
from django.views.generic import ListView


# Create your views here.
def home_view(request):
    return render(request, 'home.html')
