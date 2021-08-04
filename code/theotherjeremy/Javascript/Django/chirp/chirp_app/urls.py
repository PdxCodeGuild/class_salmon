from django.urls import path
from . import views

app_name = 'chirp_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_item/', views.add_item, name='add_item'),
    path('delete_item/<int:id>/', views.delete_item, name='delete_item'),
    path('user_login/', views.user_login, name='user_login')
]
