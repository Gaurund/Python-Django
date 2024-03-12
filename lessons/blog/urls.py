from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_blog, name='index_blog'),
]