from django.urls import path
from . import views

app_name = "app_grocerylist"
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.CreateItem, name='add'),
    path('delete/<int:id>', views.DeleteItem, name='delete'),
    path('update_status/<int:id>', views.UpdateItemStatus, name='update')
]
