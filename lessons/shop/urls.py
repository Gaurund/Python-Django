from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_shop, name='index_shop'),
    path('order/<int:order_pk>', views.order, name='order_pk')
]