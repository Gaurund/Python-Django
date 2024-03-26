from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('user/add/', views.user_form, name='user_form'),
    path('forms/', views.many_fields_form, name='many_fields_form'),
    path('user/', views.add_user, name="add_user"),
    path('upload/', views.upload_image, name='upload_image'),
    path('db/', views.total_in_db, name='db'),
    path('view/', views.total_in_view, name='view'),
    path('template/', views.total_in_template, name='template'),
]
