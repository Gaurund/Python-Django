from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coin/', views.coin, name='coin'),
    path('coin/<int:amount_of_flips>', views.coin, name='coin'),
    path('dice/', views.dice, name='dice'),
    path('random/', views.random_num, name='random number')
]