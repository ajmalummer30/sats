# Generated by Django 4.2.8 on 2024-02-12 09:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pettycash', '0021_alter_travelclaim_approved_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelclaim',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 12, 9, 29, 22, 835401, tzinfo=datetime.timezone.utc)),
        ),
    ]
