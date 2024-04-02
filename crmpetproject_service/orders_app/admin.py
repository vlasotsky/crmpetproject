from django.contrib import admin
from .models import Order, CoffeeMaker, Customer, CoffeeMakerInUse

# Register your models here.


class CoffeemakerAdmin(admin.ModelAdmin):
    search_fields = ("manufacturer", "model")
    list_display = ("id", "manufacturer", "model")


class CustomerAdmin(admin.ModelAdmin):
    search_fields = ("name", "addr")
    list_display = ("id", "name", "addr")


class CoffeeMakerInUseAdmin(admin.ModelAdmin):
    
    def my_customer(self, obj):
        return obj.customer.name
    
    def my_coffeemaker_model(self, obj):
        return obj.coffeemaker.model

    def my_coffeemaker_manufacturer(self, obj):
        return obj.coffeemaker.manufacturer
    
    my_customer.short_description = "Client"
    my_coffeemaker_model.short_description = "Model"
    my_coffeemaker_manufacturer.short_description = "Brand"

    search_fields = ("serial_number", "coffeemaker__manufacturer")
    raw_id_fields = ("customer", "coffeemaker")
    list_display = (
        "id",
        "my_coffeemaker_model",
        "my_coffeemaker_manufacturer",
        "serial_number",
        "status"
    )
    
    list_display = ("id", "serial_number", "customer_id", "coffeemaker_id", "status")


class OrderAdmin(admin.ModelAdmin):

    def my_coffeemaker_manufacturer(self, obj):
        return obj.coffeemaker.manufacturer
        
    def my_coffeemaker_model(self, obj): 
        return obj.coffeemaker.model

    def my_customer_name(self, obj):
        return obj.customer.name 

    def my_customer_addr(self, obj): 
        return obj.customer.name
    
    def my_serial_number(self, obj): 
        return obj.coffeemaker.serial_number
    
    my_coffeemaker_manufacturer.short_description = "Brand"
    my_coffeemaker_model.short_description = "Model"
    my_customer_name.short_description = "Client"
    my_customer_addr.short_description = "Address"
    my_serial_number.short_description = "S/n"

    list_display = (
        "id",
        "my_serial_number",
        "my_coffeemaker_model",
        "my_coffeemaker_manufacturer",
        "my_customer_name",
        "my_customer_addr",
        "date",
        "last_updated_date",
        "status",
    )

    search_fields = (
        "coffeemakerinuse__customer__name",
        "coffeemakerinuse__id",
        "coffeemakerinuse__serial_number",
        "coffeemakerinuse__coffeemaker__model",
        "coffeemakerinuse__coffeemaker__manufacturer"
    )

    raw_id_fields = ("coffeemaker",)

admin.site.register(CoffeeMaker, CoffeemakerAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(CoffeeMakerInUse, CoffeeMakerInUseAdmin)
admin.site.register(Order, OrderAdmin)
