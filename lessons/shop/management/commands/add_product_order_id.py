from django.core.management.base import BaseCommand
from shop.models import Order, Product


class Command(BaseCommand):
    help = 'Update the order by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')
        parser.add_argument('--product', type=int, help='Product ID')
        parser.add_argument('--quantity', type=int, help='Quantity of the product', default=1)

    def handle(self, *args, **options):
        pk = options.get('pk')
        order = Order.objects.filter(pk=pk).first()
        product_pk = options.get('--product')
        quantity = options.get('--quantity')
        product = Product.objects.filter(pk=product_pk).first()
        order.products.add(product, quantity=quantity)

        self.stdout.write(f'The product was added to the order.')
