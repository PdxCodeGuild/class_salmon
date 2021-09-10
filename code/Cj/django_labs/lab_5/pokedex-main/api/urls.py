from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PokemonViewSet, TypeViewSet, SoundEffectViewSet, UsersViewSet, CurrentUserView

router = DefaultRouter()
router.register('pokemon', PokemonViewSet, basename='pokemon')
router.register('types', TypeViewSet, basename='types')
router.register('sound_effects', SoundEffectViewSet, basename='sound_effects')
router.register('users', UsersViewSet, basename='users')

urlpatterns = router.urls + [
   path('currentuser/', CurrentUserView.as_view())
]
