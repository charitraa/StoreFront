# Generated by Django 4.2.5 on 2023-12-04 10:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.UUIDField(default=uuid.UUID('6cba4544-e6f6-4a08-a6df-950c79b9aeeb'), primary_key=True, serialize=False),
        ),
    ]
