from django.urls import path
from . import views

app_name = 'url_shortener_app' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('SubmitUrl', views.submit_url, name='new_url'),
    path('SubmitUrl', views.submit_url, name='code_for_url'),
    path('<str:from_user>/', views.url_by_code, name='url_by_code'),
]