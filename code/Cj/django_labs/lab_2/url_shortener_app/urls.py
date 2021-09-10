from django.urls import path
from . import views

app_name = 'url_shortener'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('addurl/', views.add_url, name = 'add_url'),
    path('<str:short_url>', views.visit_url, name = 'visit_url'),

]