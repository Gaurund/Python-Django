import datetime

from django.db.models import F
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Order, Client, OrderProduct, Product
import logging

logger = logging.getLogger(__name__)


def index_shop(request):
    template_name = "shop/index.html"
    logger.info('Shop page accessed')

    week_orders = Order.objects.all()
    order_products = OrderProduct.objects.all()
    products = Product.objects.all()

    context = {
        'title': "Магазинчик Бо",
        'orders': week_orders,
        'products': products,
        'order_products': order_products
    }

    return render(
        request,
        template_name,
        context
    )


def order(request, order_pk):
    template_name = "shop/order.html"
    order = Order.objects.get(pk=order_pk)
    op_list = OrderProduct.objects.filter(order_id=order_pk).select_related("product")

    context = {
        'title': "Заказ номер ",
        'order_pk': order_pk,

        'order': order,
        'op_list': op_list,
    }

    return render(
        request,
        template_name,
        context
    )


def client(request, client_pk):
    template_name = "shop/client.html"
    client = Client.objects.get(id=client_pk)
    orders = Order.objects.filter(client=client).order_by('date')
    context = {
        'title': "Клиент № ",
        'client': client,
        'orders': orders
    }

    return render(
        request,
        template_name,
        context
    )


def client_week(request, client_pk):
    template_name = "shop/client.html"
    client = Client.objects.get(id=client_pk)
    week = datetime.datetime.now() - datetime.timedelta(days=7)
    orders = Order.objects.filter(client=client, date__gte=week).order_by('date')
    context = {
        'title': "Клиент № ",
        'client': client,
        'orders': orders
    }

    return render(
        request,
        template_name,
        context
    )


def client_month(request, client_pk):
    template_name = "shop/client.html"
    client = Client.objects.get(id=client_pk)
    week = datetime.datetime.now() - datetime.timedelta(days=30)
    orders = Order.objects.filter(client=client, date__gte=week).order_by('date')
    context = {
        'title': "Клиент № ",
        'client': client,
        'orders': orders
    }

    return render(
        request,
        template_name,
        context
    )


def client_year(request, client_pk):
    template_name = "shop/client.html"
    client = Client.objects.get(id=client_pk)
    week = datetime.datetime.now() - datetime.timedelta(days=365)
    orders = Order.objects.filter(client=client, date__gte=week).order_by('date')
    context = {
        'title': "Клиент № ",
        'client': client,
        'orders': orders
    }

    return render(
        request,
        template_name,
        context
    )
