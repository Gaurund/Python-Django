import datetime

from django.core.files.storage import FileSystemStorage
from django.db.models import F
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .forms import ProductForm
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

    products = []

    for order in orders:
        product_list = OrderProduct.objects.filter(order_id=order.pk).select_related("product")
        for product in product_list:
            if product.product.name not in products:
                products.append(product.product.name)

    products = sorted(products)

    context = {
        'title': "Клиент № ",
        'client': client,
        'orders': orders,
        'products': products
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
    products = []

    for order in orders:
        product_list = OrderProduct.objects.filter(order_id=order.pk).select_related("product")
        for product in product_list:
            if product.product.name not in products:
                products.append(product.product.name)

    products = sorted(products)

    context = {
        'title': "Клиент № ",
        'client': client,
        'orders': orders,
        'products': products
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
    products = []

    for order in orders:
        product_list = OrderProduct.objects.filter(order_id=order.pk).select_related("product")
        for product in product_list:
            if product.product.name not in products:
                products.append(product.product.name)

    products = sorted(products)

    context = {
        'title': "Клиент № ",
        'client': client,
        'orders': orders,
        'products': products
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
    products = []

    for order in orders:
        product_list = OrderProduct.objects.filter(order_id=order.pk).select_related("product")
        for product in product_list:
            if product.product.name not in products:
                products.append(product.product.name)

    products = sorted(products)

    context = {
        'title': "Клиент № ",
        'client': client,
        'orders': orders,
        'products': products
    }

    return render(
        request,
        template_name,
        context
    )


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            Product(**form.cleaned_data).save()
            image = form.cleaned_data['image']
            if image:
                fs = FileSystemStorage()
                fs.save(image.name, image)
            logger.info(f'Продукт внесён в базу')

    else:
        form = ProductForm()
        message = 'Введите данные продукта'

    context = {
        'title': 'Продукт',
        'form': form,
        'message': message,
    }
    template_name = 'shop/add_product.html'

    return render(
        request,
        template_name,
        context
    )
