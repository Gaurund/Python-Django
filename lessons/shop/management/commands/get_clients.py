from django.core.management.base import BaseCommand
from shop.models import Client


class Command(BaseCommand):
    help = 'Return a list of clients.'

    def handle(self, *args, **options):
        clients = Client.objects.all()
        self.stdout.write(f"{clients}")