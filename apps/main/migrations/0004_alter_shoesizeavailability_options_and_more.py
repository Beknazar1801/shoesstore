# Generated by Django 5.1.2 on 2024-11-29 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_shoes_available_quantity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoesizeavailability',
            options={'verbose_name': 'Наличие обуви', 'verbose_name_plural': 'Наличие обуви'},
        ),
        migrations.RemoveField(
            model_name='shoes',
            name='available_quantity',
        ),
        migrations.AlterField(
            model_name='shoesizeavailability',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='shoesizeavailability',
            name='shoe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.shoes', verbose_name='Обувь'),
        ),
        migrations.AlterField(
            model_name='shoesizeavailability',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.shoesize', verbose_name='Размер'),
        ),
    ]
