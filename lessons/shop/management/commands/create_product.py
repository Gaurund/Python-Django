import decimal

from django.core.management.base import BaseCommand
from shop.models import Product


class Command(BaseCommand):
    help = "Create a product at the shop"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name of the product')
        parser.add_argument('description', type=str, help='description of the product')
        parser.add_argument('price', type=float, help='price')
        parser.add_argument('quantity', type=int, help='amount')

    def handle(self, *args, **options):
        name = options.get('name')
        description = options.get('description')
        price = options.get('price')
        quantity = options.get('quantity')

        product = Product(
            name=name,
            description=description,
            price=price,
            quantity=quantity,
        )

        product.save()
        self.stdout.write(f'The product was added.')
