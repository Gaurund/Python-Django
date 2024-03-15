from django.db import models
from django.utils import timezone
# from django.db.models import Sum, F


class Client(models.Model):
    name = models.CharField(max_length=100, default="Best client ever")
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=256)
    registered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Full name: {self.name}. E-mail: {self.email}. Registered since: {self.registered}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="Description is currently unavailable.")
    price = models.DecimalField(max_digits=16, decimal_places=2)
    quantity = models.IntegerField()
    was_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Name: {self.name}, price: {self.price}, quantity: {self.quantity}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct', related_name='ord_pro')
    total = models.DecimalField(max_digits=16, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.client.name} ordered {self.products}'

    # def save(self, *args, **kwargs):
    #     query = OrderProduct.objects.filter(order=self).annotate(
    #         sub_total=F('quantity') * F('product__price')
    #     ).aggregate(result=Sum('sub_total'))
    #
    #     self.total = round(query['result'], 2)
    #     super(Order, self).save()


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    op_quantity = models.IntegerField(default=1)
