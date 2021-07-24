from django.urls import path
from . import views

app_name = 'grocery_list'
urlpatterns = [
    path('', views.index, name='grocery_list'),
    path('add/', views.addItem, name='add'),
    path('delete/<int:id>', views.deleteItem, name='deleteItem')
]
    