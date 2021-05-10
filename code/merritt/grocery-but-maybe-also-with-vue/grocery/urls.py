from django.urls import path

from . import views

app_name = 'grocery'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_item, name='add_item'),
    path('complete/<int:pk>/', views.mark_complete, name='mark_complete'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]