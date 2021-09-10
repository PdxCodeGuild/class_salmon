from django.urls import path

from .views import CurrentPokemonView, PokemonViewSet, TypeViewSet, CurrentUserView, UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('pokemon',PokemonViewSet, basename='pokemon')
router.register('type',TypeViewSet, basename='type')
router.register('users',UserViewSet, basename='users')
urlpatterns = router.urls + [
    path('currentuser/', CurrentUserView.as_view())
]

""" urlpatterns = [
    path('', ListPokemon.as_view()),
    path('<int:pk>/', DetailPokemon.as_view()),
] """