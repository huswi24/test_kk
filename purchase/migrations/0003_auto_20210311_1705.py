# Generated by Django 3.0.8 on 2021-03-11 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_sale_available'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sale',
            options={'verbose_name_plural': '売上データ'},
        ),
    ]
