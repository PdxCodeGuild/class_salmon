from django.urls import path

from . import views

app_name = 'grocery'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('complete/<int:pk>/', views.complete, name='complete'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]