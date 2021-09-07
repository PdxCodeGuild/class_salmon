from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PokemonViewSet, TypeViewSet, UserViewSet

router = DefaultRouter()
router.register('pokemon', PokemonViewSet, basename='pokemon')
router.register('type', TypeViewSet, basename='type')
router.register('users', UserViewSet, basename='users')

urlpatterns = router.urls