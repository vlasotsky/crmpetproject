import datetime
from typing import Iterable
from django.db import models

# Create your models here.


class CoffeeMaker(models.Model):

    # Device class

    class Meta:
        db_table = "coffeemakers"
        verbose_name = "New coffeemaker"
        verbose_name_plural = "Available coffeemakers"

    manufacturer = models.TextField(verbose_name="Manufacturer")
    model = models.TextField(verbose_name="Model")

    def __str__(self) -> str:
        return f"{self.manufacturer} {self.model}"


class Customer(models.Model):

    class Meta:
        db_table = "customers"
        verbose_name = "New customer"
        verbose_name_plural = "Customers' details"

    name = models.TextField(verbose_name="Name")
    addr = models.TextField(verbose_name="Address")

    def __str__(self) -> str:
        return f"{self.name} with address: {self.addr}"


class CoffeeMakerInUse(models.Model):

    class Meta:
        db_table = "coffeemakers_in_use"
        verbose_name = "New coffeemaker"
        verbose_name_plural = "Coffeemakers currently in use"

    serial_number = models.TextField(verbose_name="Serial number")
    customer = models.ForeignKey(
        Customer, on_delete=models.RESTRICT, verbose_name="Owner ID"
    )
    coffeemaker = models.ForeignKey(
        CoffeeMaker, on_delete=models.RESTRICT, verbose_name="Coffeemaker ID"
    )
    status = models.TextField(verbose_name="Ownership status")

    def __str__(self) -> str:
        return f"{self.serial_number}: {self.status}"


class Order(models.Model):

    statuses = (
        ("sold", "sold"),
        ("returned", "returned"),
        ("guarantee repair", "warranty repair"),
        ("waiting for payment", "not payed"),
    )

    class Meta:
        db_table = "orders"
        verbose_name = "New order"
        verbose_name_plural = "Orders"

    customer = models.ForeignKey(
        Customer, on_delete=models.RESTRICT, verbose_name="Customer ID"
    )
    coffeemaker = models.ForeignKey(
        CoffeeMaker, on_delete=models.RESTRICT, verbose_name="Coffeemaker ID"
    )
    date = models.DateTimeField(verbose_name="Date and time created", auto_now_add=True)

    last_updated_date = models.DateTimeField(
        verbose_name="Last updated", blank=True, null=True
    )
    status = models.TextField(verbose_name="Order status", choices=statuses)

    def save(
        self, *args, **kwargs
    ):  # redefining function to have the last updated date save
        self.last_updated_date = datetime.now()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.id}, {self.coffeemaker}"
