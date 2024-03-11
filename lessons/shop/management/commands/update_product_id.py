from django.core.management.base import BaseCommand
from shop.models import Product

class Command(BaseCommand):
    help = 'Update a product by ID.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=str, help='Product ID')
        parser.add_argument('--name', type=str, help='New name')
        parser.add_argument('--description', type=str, help='New description')
        parser.add_argument('--price', type=float, help='New price')
        parser.add_argument('--quantity', type=int, help='New amount')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        if product is None:
            return f"No such product was found"
        name = kwargs.get('name')
        if name is not None:
            product.name = name

        description = kwargs.get('description')
        if description is not None:
            product.description = description

        price = kwargs.get('price')
        if price is not None:
            product.price = price

        quantity = kwargs.get('quantity')
        if quantity is not None:
            product.quantity = quantity

        product.save()
        self.stdout.write(f'{product}')