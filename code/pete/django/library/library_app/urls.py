from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
  path('', views.index, name='index'),
  path('add-author/', views.add_author, name='add_author'),
  path('author/<int:id>/', views.author_detail, name='author'),
  path('add-book/<int:author_id>/', views.add_book, name='add_book'),
  # add delete path here
]