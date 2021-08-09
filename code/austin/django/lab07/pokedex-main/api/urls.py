from django.urls import path

from .views import PokemonViewSet, TypeViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('pokemon',PokemonViewSet, basename='pokemon')
router.register('type',TypeViewSet, basename='type')
urlpatterns = router.urls

""" urlpatterns = [
    path('', ListPokemon.as_view()),
    path('<int:pk>/', DetailPokemon.as_view()),
] """