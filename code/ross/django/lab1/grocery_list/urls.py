from . import views
from django.contrib import admin
from django.urls import path, include

app_name = 'grocery_list'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('complete/<int:pk>/', views.complete, name='complete'),
    path('delete/<int:pk>', views.delete, name='delete'),
    # path('<int:edit_list>/new_item', views.new_item, name='new_item'),
    # path('', include(('index.urls', 'index'), namespace='index'))
]