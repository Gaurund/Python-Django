from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_task5, name='index_task5'),
    path('coin/', views.coin, name='coin'),
    path('coin/<int:amount_of_flips>', views.coin, name='coin'),
    path('dice/', views.dice, name='dice'),
    path('dice/<int:amount_of_toss>', views.dice, name='dice'),
    path('random/', views.random_num, name='random number'),
    path('random/<int:amount_of_rand>', views.random_num, name='random number'),
    path('game/', views.game, name="game"),
]