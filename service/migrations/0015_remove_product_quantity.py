# Generated by Django 2.2 on 2019-12-16 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0014_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]
