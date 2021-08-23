from django.urls import path
from .views import ListPokemon, DetailPokemon

urlpatterns = [
    path("", ListPokemon.as_view()),
    path("<int:pk>/", DetailPokemon.as_view()),
]
