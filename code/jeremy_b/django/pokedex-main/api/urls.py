from django.urls import path, include
from rest_framework import routers

from .views import PokemonViewSet, TypeViewSet, UserViewSet, UserView


app_name = 'main'

router = routers.DefaultRouter()
router.register('pokemon', PokemonViewSet, basename="pokemon")
router.register('type', TypeViewSet, basename="types")
router.register('users', UserViewSet, basename="users")

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/current_user/', UserView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]