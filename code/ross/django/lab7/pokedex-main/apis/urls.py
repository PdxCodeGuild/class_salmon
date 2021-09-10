from django.urls import path

from .views import PokemonViewSet, TypeViewSet, CurrentPokemonView, UserViewSet # ListPokemon, DetailPokemon, ListType, DetailType
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('pokemon', PokemonViewSet, basename='pokemon')
router.register('type', TypeViewSet, basename='type')
router.register('users', UserViewSet, basename='users')

urlpatterns = router.urls + [
    path('currentpokemon/', CurrentPokemonView.as_view())
]

# urlpatterns = [
#     path('', ListPokemon.as_view()),
#     path('<int:pk>/', DetailPokemon.as_view()),
#     path('type', ListType.as_view()),
#     path('<int:pk>/', DetailType.as_view()),
# ]