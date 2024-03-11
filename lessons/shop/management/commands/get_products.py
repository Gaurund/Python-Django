from django.core.management.base import BaseCommand
from shop.models import Product


class Command(BaseCommand):
    help = 'Return a list of clients.'

    def handle(self, *args, **options):
        product = Product.objects.all()
        self.stdout.write(f"{product}")
