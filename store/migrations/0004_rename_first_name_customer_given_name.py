<<<<<<< HEAD
# Generated by Django 4.2.5 on 2023-10-11 11:07
=======
# Generated by Django 4.2.5 on 2023-10-11 08:42
>>>>>>> a8a07f46a78d3677667150498813c74b98bf7065

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='given_name',
        ),
    ]
