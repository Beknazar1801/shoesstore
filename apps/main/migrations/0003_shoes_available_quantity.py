# Generated by Django 5.1.2 on 2024-11-29 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_shoesizeavailability'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoes',
            name='available_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
