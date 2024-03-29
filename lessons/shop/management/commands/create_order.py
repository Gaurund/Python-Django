import decimal

from django.core.management.base import BaseCommand
from shop.models import Order, Product, Client


class Command(BaseCommand):
    help = "Create an order at the shop"

    def add_arguments(self, parser):
        parser.add_argument('client_pk', type=int, help='Client ID')
        parser.add_argument('product_pk', type=int, help='Product ID')
        parser.add_argument('quantity', nargs='?', type=int, help='Product quantity', default=1)

    def handle(self, *args, **options):
        client_pk = options.get('client_pk')
        product_pk = options.get('product_pk')
        quantity = options.get('quantity')

        client = Client.objects.filter(pk=client_pk).first()
        product = Product.objects.filter(pk=product_pk).first()

        order = Order(
            client=client,
            quantity=quantity,
            total=product.price
        )
        order.save()
        order.products.add(product)
        self.stdout.write(f'The product was added.')
