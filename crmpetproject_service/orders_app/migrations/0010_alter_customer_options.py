# Generated by Django 3.2.8 on 2024-04-02 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders_app', '0009_auto_20240402_1451'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'customer', 'verbose_name_plural': 'Customer info'},
        ),
    ]