from django.core.management.base import BaseCommand
from shop.models import Product


class Command(BaseCommand):
    help = 'Return a product by ID.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=str, help='Product ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        self.stdout.write(f'{product}')
