# Generated by Django 4.2.8 on 2024-04-28 12:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itassets', '0044_alter_it_prodcuts_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='it_prodcuts',
            name='created_date',
            field=models.DateField(default=datetime.date(2024, 4, 28)),
        ),
    ]
