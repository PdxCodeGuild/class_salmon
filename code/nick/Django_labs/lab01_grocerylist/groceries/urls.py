from django.urls import path
from . import views

app_name = 'groceries' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),#when they start go to views, route name is index
    path('AddGrocery', views.add_grocery, name='new_item'),
    path('DeleteGrocery/<int:id>', views.delete_grocery, name='delete_item'),
]