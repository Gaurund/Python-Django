import datetime

from django.core.management.base import BaseCommand
from shop.models import Order, Client, OrderProduct, Product
import shop.utils
from faker import Faker
from random import randint, choice, uniform, randrange

fake = Faker('ru_RU')


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


def registered():
    start = datetime.date(2000, 1, 1)
    end = datetime.date(2012, 12, 31)
    return random_date(start, end)

def was_added():
    start = datetime.date(2013, 1, 1)
    end = datetime.date(2014, 12, 31)
    return random_date(start, end)

def order_date():
    start = datetime.date(2023, 1, 1)
    end = datetime.date(2024, 3, 14)
    return random_date(start, end)
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
                email=fake.unique.email(),
                phone=shop.utils.mutate_phone_number(fake.unique.phone_number()),
                address=fake.address(),
                registered=registered()
            )
            client.save()
            clients.append(client)

        products = []
        for p in self.PRODUCTS:
            product = Product(
                name=p,
                description=p,
                price=randint(10, 300),
                quantity=self.PRODUCTS_AMOUNT,
                was_added=was_added(),
            )
            product.save()
            products.append(product)

        for client in clients:
            for _ in range(self.ORDERS_PER_PERSON):
                order = Order(client=client,
                              total=0,
                              date=order_date()
                              )
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
                        quantity=quantity,
                    ).save()
                order.total = total
                order.save()
        self.stdout.write(f"Fake data created!")
