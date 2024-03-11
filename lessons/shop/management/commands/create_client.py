from django.core.management.base import BaseCommand
from shop.models import Client
import shop.utils

class Command(BaseCommand):
    help = 'Create a client of the shop.'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Full name of the client')
        parser.add_argument('email', type=str, help='proper e-mail')
        parser.add_argument('phone', type=str, help='proper phone number')
        parser.add_argument('address', type=str, help='an address')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone = shop.utils.mutate_phone_number(kwargs.get('phone'))
        address = kwargs.get('address')

        client = Client(
            name=name,
            email=email,
            phone=phone,
            address=address,
        )
        client.save()
        self.stdout.write(f'The client was added.')
