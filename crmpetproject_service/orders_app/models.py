import datetime
from typing import Iterable
from django.db import models
from django.forms import ValidationError

# Create your models here.


class CoffeeMaker(models.Model):

    # Device class

    class Meta:
        db_table = "devices"
        verbose_name = "Available device"
        verbose_name_plural = "Available devices"

    manufacturer = models.TextField(verbose_name="Manufacturer")
    model = models.TextField(verbose_name="Model")

    def __str__(self) -> str:
        return f"{self.manufacturer} {self.model}"


class Customer(models.Model):

    class Meta:
        db_table = "customers"
        verbose_name = "Customer details"
        verbose_name_plural = "Many customers' details"

    name = models.TextField(verbose_name="Name")
    addr = models.TextField(verbose_name="Address")

    def __str__(self) -> str:
        return f"{self.name}"


class CoffeeMakerInUse(models.Model):

    class Meta:
        db_table = "coffeemakers_in_use"
        verbose_name = "Coffeemaker in use"
        verbose_name_plural = "Coffeemakers being used"

    serial_number = models.TextField(verbose_name="Serial number")
    customer_id = models.ForeignKey(
        Customer, on_delete=models.RESTRICT, verbose_name="Owner ID"
    )
    coffeemaker_id = models.ForeignKey(
        CoffeeMaker, on_delete=models.RESTRICT, verbose_name="Coffeemaker ID"
    )
    status = models.TextField(verbose_name="Ownership status")

    def __str__(self) -> str:
        return f"{self.serial_number} {self.status}"


# func to validate values of status variable to avoid values out of context
def validate_status(status: str):
    if status not in ["sold", "returned", "guarantee repair", "waiting for payment"]:
        raise ValidationError(
            f"{status.upper} is out of valid status options.\nPlease, type another one",
            params=f"order status: {status}",
        )


class Order(models.Model):

    class Meta:
        db_table = "orders"
        verbose_name = "Single order"
        verbose_name_plural = "Orders"

    customer_id = models.ForeignKey(
        Customer, on_delete=models.RESTRICT, verbose_name="Customer ID"
    )
    coffeemaker_id = models.ForeignKey(
        CoffeeMaker, on_delete=models.RESTRICT, verbose_name="Coffeemaker ID"
    )
    date = models.DateTimeField(verbose_name="Date and time created", auto_now_add=True)

    last_updated_date = models.DateTimeField(
        verbose_name="Last updated", blank=True, null=True
    )
    status = models.TextField(verbose_name="Order status", validators=[validate_status])

    # redefining function to have the last updated date save
    def save(self, *args, **kwargs):
        self.last_updated_date = datetime.now()
        super().save(*args, **kwargs)
