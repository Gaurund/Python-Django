from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_shop, name='index_shop'),
]