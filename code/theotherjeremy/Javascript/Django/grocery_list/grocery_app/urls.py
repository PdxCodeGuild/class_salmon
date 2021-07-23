from django.urls import path
from . import views

# app_name is url user will type (grocery_app)
app_name = 'grocery_app'
urlpatterns = [

    path('', views.index, name='index'),
    # path('rando', views.rando, name='rando'),

    path('new_item/', views.add_item, name='new_item'),


]
