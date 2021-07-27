from django.urls import path
from url_shortener import views

app_name = 'url_shortener'

urlpatterns = [
    path('', views.index, name='index'),
    path('shorty', views.shorty, name='shorty')
]
