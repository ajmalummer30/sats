# Generated by Django 4.2.8 on 2024-05-07 08:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0183_alter_checklistdetails_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistdetails',
            name='time',
            field=models.TimeField(default='11:38:02'),
        ),
        migrations.AlterField(
            model_name='workers',
            name='upload_Iqama',
            field=models.FileField(blank=True, null=True, upload_to='WorkPermit_iqama/'),
        ),
        migrations.AlterField(
            model_name='workpermit',
            name='Created_time',
            field=models.TimeField(default=datetime.datetime(2024, 5, 7, 8, 38, 2, 38073, tzinfo=datetime.timezone.utc)),
        ),
    ]
