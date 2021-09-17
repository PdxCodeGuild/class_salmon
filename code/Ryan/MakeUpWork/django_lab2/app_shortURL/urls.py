from django.urls import path
from . import views

app_name = "app_shortURL"

urlpatterns = [
    path('', views.home, name="app-home"),
    path('test/', views.test, name="app-test"),
    path('redirect/', views.RedirectURL, name="app-redirect"),
    path("encrypt/", views.URLEncryption, name="app-encrypt")
]
