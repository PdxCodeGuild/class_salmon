from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CurrentUserView, PokemonViewSet, TypeViewSet, UserViewSet

router = DefaultRouter()
router.register('pokemon', PokemonViewSet, basename='pokemon')
# router.register('users', UserViewSet, basename='users')
router.register('types', TypeViewSet, basename='types')
router.register('users', UserViewSet, basename='users')

urlpatterns = router.urls + [
    path('currentuser/', CurrentUserView.as_view())
]