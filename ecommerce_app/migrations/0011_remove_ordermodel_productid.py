# Generated by Django 4.2.1 on 2023-08-15 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0010_ordermodel_remove_cart_is_buy_cart_orderid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='productId',
        ),
    ]
