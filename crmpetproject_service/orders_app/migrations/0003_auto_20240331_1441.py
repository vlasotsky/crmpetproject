# Generated by Django 3.2.8 on 2024-03-31 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders_app', '0002_coffeemaker_coffeemakerinuse_customer_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coffeemaker',
            options={'verbose_name': 'Available coffeemaker', 'verbose_name_plural': 'Available coffeemakers'},
        ),
        migrations.AlterModelTable(
            name='coffeemaker',
            table='coffeemakers',
        ),
    ]
