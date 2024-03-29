# Generated by Django 4.2.5 on 2023-11-27 10:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_collection_options_alter_customer_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='promotions',
            field=models.ManyToManyField(blank=True, to='store.promotion'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.CharField(max_length=300, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
    ]
