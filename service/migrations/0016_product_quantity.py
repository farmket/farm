# Generated by Django 2.2 on 2019-12-16 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0015_remove_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
