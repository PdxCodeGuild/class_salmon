from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PokemonViewSet, TypeViewSet

router = DefaultRouter()
router.register('pokemon', PokemonViewSet, basename='pokemon')
# router.register('users', UserViewSet, basename='users')
router.register('types', TypeViewSet, basename='types')

urlpatterns = router.urls
