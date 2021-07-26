from django.urls import path
from . import views

app_name = 'grocery'
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:list_id>/detail/', views.list_detail, name='list_detail'),
    path('add_list', views.add_list, name='add_list'),
    path('edit_list', views.edit_list, name='edit_list'),
    path('request_complete', views.request_complete, name='request_complete'),
    path('add_list_item/<int:pk>', views.add_list_item, name='add_list_item'),
    path('edit_list/<int:list_id>', views.edit_list, name='edit_list'),
    path('delete_list/<int:list_id>', views.delete_list, name='delete_list'),
    path('disable_list/<int:list_id>', views.list_disable, name='disable_list'),
    path('enable_list/<int:list_id>', views.list_enable, name='enable_list'),
    path('delete_item/<int:item_id>', views.delete_list_item, name='delete_list_item'),
    path('item_complete/<int:item_id>', views.item_complete, name="item_complete")
]