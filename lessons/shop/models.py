from django.db import models
from django.utils import timezone


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
        return f'{self.name}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total = models.DecimalField(max_digits=16, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.client.name} ordered {self.products}'