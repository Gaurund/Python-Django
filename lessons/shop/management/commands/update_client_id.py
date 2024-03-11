from django.core.management.base import BaseCommand
from shop.models import Client
import shop.utils


class Command(BaseCommand):
    help = 'Update a client by ID.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=str, help='Client ID')
        parser.add_argument('--name', type=str, help='New name')
        parser.add_argument('--email', type=str, help='New e-mail')
        parser.add_argument('--phone', type=str, help='New phone number')
        parser.add_argument('--address', type=str, help='New address')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        if client is None:
            return f"No such client was found"
        name = kwargs.get('name')
        if name is not None:
            client.name = name

        email = kwargs.get('email')
        if email is not None:
            client.email = email

        phone = kwargs.get('phone')
        if phone is not None:
            client.phone = shop.utils.mutate_phone_number(phone)

        address = kwargs.get('address')
        if address is not None:
            client.address = address

        client.save()
        self.stdout.write(f'{client}')

