# Generated by Django 4.2.5 on 2023-10-12 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_sizevariant_size_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category1', to='product.category'),
        ),
    ]
