# Generated by Django 4.2.3 on 2023-08-24 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
