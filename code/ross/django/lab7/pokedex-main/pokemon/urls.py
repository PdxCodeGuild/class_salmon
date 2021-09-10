from . import views
from django.urls import path, include
from django.views.generic import TemplateView

app_name = "pokemon"

urlpatterns = [
    # path('catch/', TemplateView.as_view(template_name='home.html'), name='catch'),
    # path('catch/<int:pk>', views.catch, name='catch'),
    # path('catch/', views.catch, name='catch'),
]
