# Generated by Django 4.2.8 on 2024-02-09 18:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pettycash', '0018_travelclaim_approved_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelclaim',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 9, 18, 4, 49, 630380, tzinfo=datetime.timezone.utc)),
        ),
    ]
