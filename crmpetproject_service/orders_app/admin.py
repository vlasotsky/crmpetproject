from django.contrib import admin
from .models import Order, CoffeeMaker, Customer, CoffeeMakerInUse

# Register your models here.


class CoffeemakerAdmin(admin.ModelAdmin):
    list_display = ("id", "manufacturer", "model")


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "addr")


class CoffeeMakerInUseAdmin(admin.ModelAdmin):
    list_display = ("id", "serial_number", "customer_id",
                    "coffeemaker_id", "status")


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'customer_id',
        "coffeemaker_id",
        "date",
        "last_updated_date",
        "status",
    )


admin.site.register(CoffeeMaker, CoffeemakerAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(CoffeeMakerInUse, CoffeeMakerInUseAdmin)
admin.site.register(Order, OrderAdmin)
