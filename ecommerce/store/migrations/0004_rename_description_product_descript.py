# Generated by Django 4.2.3 on 2023-08-24 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='descript',
        ),
    ]
