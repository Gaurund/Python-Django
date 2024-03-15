from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('user/add/', views.user_form, name='user_form'),
    path('forms/', views.many_fields_form, name='many_fields_form'),

]