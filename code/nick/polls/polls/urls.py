from django.urls import path
from . import views

app_name = 'polls'
#has to be called urlpatterns
urlpatterns = [
    path('', views.index, name='index'),#when they start go to views, route name is index
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]
