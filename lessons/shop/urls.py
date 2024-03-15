from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_shop, name='index_shop'),
    path('order/<int:order_pk>', views.order, name='order_pk'),
    path('client/<int:client_pk>', views.client, name="client_pk"),
    path('client/<int:client_pk>/week/', views.client_week, name="client_week"),
    path('client/<int:client_pk>/month/', views.client_month, name="client_month"),
    path('client/<int:client_pk>/year/', views.client_year, name="client_year"),
]