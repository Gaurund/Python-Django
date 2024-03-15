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


def order_date():
    start = datetime.datetime(2024, 2, 14, 0, 0, 0)
    end = datetime.datetime(2024, 3, 14, 0, 0, 0)
    return random_date(start, end)


class Command(BaseCommand):
    help = "Generate fake data for User "
    PRODUCTS = [
        'Картофель', 'Морковь', 'Лук', 'Чеснок', 'Петрушка', 'Укроп', 'Яблоки', 'Бананы', 'Лимон',
        'Масло сливочное', 'Кефир', 'Молоко', 'Сметана', 'Творог', 'Сыр',
        'Горчица', 'Малиновое варенье', 'Томатная паста', 'Рыбная консерва', 'Консервированный горошек',
        'Консервированная кукуруза', 'Сгущенка', 'Мед',
    ]
    ORDERS_PER_PERSON = 5
    PRODUCTS_PER_ORDER = 5
    MAX_PRODUCTS_IN_ORDER = 5
    PRODUCTS_AMOUNT = 100

    # def add_arguments(self, parser):
    #     parser.add_argument('count', type=int, help='Amount of fake data')

    def handle(self, *args, **options):
        # count = options['count']
        clients = Client.objects.all()
        products = Product.objects.all()
        for client in clients:
            for _ in range(self.ORDERS_PER_PERSON):
                order = Order(client=client,
                              total=0,
                              date=order_date()
                              )
                order.save()

                total = 0
                for _ in range(self.PRODUCTS_PER_ORDER):
                    # prod_list = order.products
                    random_product = choice(products)
                    # while random_product.pk in prod_list:
                    #     random_product = choice(products)
                    quantity = randint(1, self.MAX_PRODUCTS_IN_ORDER)
                    total += quantity * random_product.price
                    OrderProduct(
                        order=order,
                        product=random_product,
                        op_quantity=quantity,
                    ).save()
                order.total = total
                order.save()
        self.stdout.write(f"Fake data created!")
