from django.urls import path

from .views import ListTeams, DetailTeam

urlpatterns = [
    path('', ListTeams.as_view()),
    path('<int:pk>/', DetailTeam.as_view())
]
