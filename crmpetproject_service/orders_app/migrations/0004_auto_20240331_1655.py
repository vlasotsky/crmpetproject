# Generated by Django 3.2.8 on 2024-03-31 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders_app', '0003_auto_20240331_1441'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coffeemakerinuse',
            options={'verbose_name': 'Coffeemaker in use', 'verbose_name_plural': 'Coffeemakers currently used'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'Customer details', 'verbose_name_plural': "Customers' details"},
        ),
    ]
