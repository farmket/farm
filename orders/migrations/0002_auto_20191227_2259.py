# Generated by Django 2.2 on 2019-12-27 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_no',
            field=models.CharField(max_length=11),
        ),
    ]
