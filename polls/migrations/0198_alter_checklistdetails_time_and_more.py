# Generated by Django 4.2.8 on 2024-05-17 10:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0197_alter_checklistdetails_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistdetails',
            name='time',
            field=models.TimeField(default='13:08:55'),
        ),
        migrations.AlterField(
            model_name='workpermit',
            name='Created_time',
            field=models.TimeField(default=datetime.datetime(2024, 5, 17, 10, 8, 55, 449368, tzinfo=datetime.timezone.utc)),
        ),
    ]
