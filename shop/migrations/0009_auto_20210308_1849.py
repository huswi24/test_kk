# Generated by Django 3.0.8 on 2021-03-08 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_product_cartdescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cartDescription',
            field=models.TextField(blank=True, max_length=100, verbose_name='カート用説明'),
        ),
    ]
