from django.urls import path
from . import views

# app_name is url user will type (grocery_app)
app_name = 'short_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('shorten_it/', views.shorten_it, name='shorten_it'),
    path('redirect/<int:id>', views.redirect, name='redirect')
]
