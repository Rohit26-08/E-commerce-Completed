# Generated by Django 4.2.6 on 2023-12-28 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_product_image_delete_productimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_image',
        ),
    ]
