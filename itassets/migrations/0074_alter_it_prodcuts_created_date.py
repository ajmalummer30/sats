# Generated by Django 4.2.8 on 2024-06-08 09:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itassets', '0073_alter_it_prodcuts_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='it_prodcuts',
            name='created_date',
            field=models.DateField(default=datetime.date(2024, 6, 8)),
        ),
    ]
