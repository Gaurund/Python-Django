from django.contrib import admin
from .models import *


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'phone',
        'registered',
    ]

    search_fields = ['name']

    ordering = ['name', '-registered']


class OrderInlineAdmin(admin.TabularInline):
    model = Order.products.through

    readonly_fields = [
        'product',
        'op_quantity',
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'client',
        'total',
        'date',
    ]

    readonly_fields = [
        'total',
        'date',
    ]

    inlines = (OrderInlineAdmin,)


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'quantity',
    ]

    list_filter = [
        'price',
        'quantity',
    ]

    search_fields = ['name']

    actions = [reset_quantity]
