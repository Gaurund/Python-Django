from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('headtails/', views.headtails, name='headtails'),
    path('dice/', views.dice, name='dice'),
    path('random/', views.random_num, name='random number')
]