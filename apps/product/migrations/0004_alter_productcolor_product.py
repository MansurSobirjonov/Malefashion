# Generated by Django 3.2.13 on 2022-06-16 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20220616_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcolor',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_color', to='product.product'),
        ),
    ]
