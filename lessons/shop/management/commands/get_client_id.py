from django.core.management.base import BaseCommand
from shop.models import Client


class Command(BaseCommand):
    help = 'Return a client by ID.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=str, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        self.stdout.write(f'{client}')