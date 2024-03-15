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

    logger.info('Shop page accessed')

    order = Order.objects.get(pk=order_pk)
    order_products = OrderProduct.objects.filter(order_id=order_pk)
    # products = Product.objects.all()
    product_list = []
    quantity_list = []
    for op in order_products:
        product_list.append(Product.objects.get(pk=op.product_id))

    # op_list = OrderProduct.objects.filter(order_id=order_pk).annotate(product__name=F('product__name'))
    op_list = OrderProduct.objects.filter(order_id=order_pk).select_related("product")

    context = {
        'title': "Заказ номер ",
        'order_pk': order_pk,

        'order': order,
        'order_products': order_products,
        'product_list': product_list,
        'op_list': op_list,
    }

    return render(
        request,
        template_name,
        context
    )
