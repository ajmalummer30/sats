# Generated by Django 4.2.8 on 2024-10-04 20:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0249_alter_checklistdetails_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistdetails',
            name='time',
            field=models.TimeField(default='23:41:57'),
        ),
        migrations.AlterField(
            model_name='workpermit',
            name='Created_time',
            field=models.TimeField(default=datetime.datetime(2024, 10, 4, 20, 41, 57, 711643, tzinfo=datetime.timezone.utc)),
        ),
    ]
