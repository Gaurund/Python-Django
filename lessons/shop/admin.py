from django.contrib import admin
from .models import *

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(OrderProduct)


# admin.site.register(Order)

class OrderProductFilter(admin.SimpleListFilter):
    # def lookups(self, request, model_admin):
    #     return OrderProduct.objects.filter(order_id=request.order.pk).select_related("product")

    def queryset(self, request, model_admin):
        return OrderProduct.objects.filter(order_id=request.order.pk).select_related("product")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'client',
        'total',
        'date',

    ]

    # list_filter = [OrderProductFilter]

    readonly_fields = [
        'total',
        'date',
    ]

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['client', 'total', 'date']
            }
        ),
        # (
        #     'Продукты',
        #     {
        #         'classes': ['wide'],
        #         'fields': [OrderProductFilter]
        #     }
        # )
    ]

