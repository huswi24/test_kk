# Generated by Django 3.0.8 on 2021-03-06 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200902_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='inTax',
            field=models.PositiveIntegerField(default=200),
        ),
    ]
