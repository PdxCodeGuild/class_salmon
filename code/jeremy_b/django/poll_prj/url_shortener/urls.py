from django.urls import path
from . import views


app_name = 'url_shortener'
urlpatterns = [
    path('', views.index, name="index"),
    path('add_url', views.add_new_url, name="add_url"),
    path('edit_url/<int:url_id>', views.edit_url, name="edit_url"),
    path('delete_url/<int:url_id>', views.delete_url, name="delete_url"),
    path('search', views.search_url, name="search"),
    path('to/<str:shortcode>', views.url_redirect, name="redirect"),
]