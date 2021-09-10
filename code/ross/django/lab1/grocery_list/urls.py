from . import views
from django.contrib import admin
from django.urls import path, include

app_name = 'grocery_list'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<item_id>', views.delete, name='delete'),
    path('complete/<item_id>', views.complete, name='complete'),
    path('new/', views.new, name='new'),
    # path('<int:edit_list>/new_item', views.new_item, name='new_item'),
    # path('', include(('index.urls', 'index'), namespace='index'))
]