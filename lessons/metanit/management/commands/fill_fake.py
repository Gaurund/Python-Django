from django.core.management.base import BaseCommand
from metanit.models import Order, Client, OrderProduct, Product
from faker import Faker
from random import randint, choice, uniform

fake = Faker('ru_RU')


class Command(BaseCommand):
    help = "Generate fake data for User "
    PRODUCTS = [
        'Картофель', 'Морковь', 'Лук', 'Чеснок', 'Петрушка', 'Укроп', 'Яблоки', 'Бананы', 'Лимон',
        'Масло сливочное', 'Кефир', 'Молоко', 'Сметана', 'Творог', 'Сыр',
        'Горчица', 'Малиновое варенье', 'Томатная паста', 'Рыбная консерва', 'Консервированный горошек',
        'Консервированная кукуруза', 'Сгущенка', 'Мед',
    ]
    ORDERS_PER_PERSON = 3
    PRODUCTS_PER_ORDER = 5
    MAX_PRODUCTS_IN_ORDER = 5
    PRODUCTS_AMOUNT = 100

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Amount of fake data')

    def handle(self, *args, **options):
        count = options['count']
        clients = []
        for _ in range(count):
            client = Client(
                name=fake.name(),
                # email=fake.unique.email(),
                # phone_number=fake.unique.phone_number().replace(' ', '').replace('(', '').replace(')', '').replace('-', ''),
                # address=fake.address(),
            )
            client.save()
            clients.append(client)

        products = []
        for p in self.PRODUCTS:
            product = Product(
                name=p,
                # description=p,
                price=randint(50, 300),
                quantity=self.PRODUCTS_AMOUNT,
            )
            product.save()
            products.append(product)

        for client in clients:
            for _ in range(self.ORDERS_PER_PERSON):
                order = Order(client=client, total=0)
                order.save()
                products_copy = products.copy()
                total = 0
                for _ in range(self.PRODUCTS_PER_ORDER):
                    random_product = choice(products_copy)
                    products_copy.remove(random_product)
                    quantity = randint(1, self.MAX_PRODUCTS_IN_ORDER)
                    total += quantity * random_product.price
                    OrderProduct(
                        order=order,
                        product=random_product,
                        order_quantity=quantity,
                    ).save()
                order.total = total
                order.save()
        self.stdout.write(f"Fake data created!")
        
