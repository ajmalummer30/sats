# Generated by Django 4.2.8 on 2024-04-09 17:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0162_gatepassmodel_image1_alter_checklistdetails_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gatepassmodel',
            name='Return_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='checklistdetails',
            name='time',
            field=models.TimeField(default='20:21:07'),
        ),
        migrations.AlterField(
            model_name='gatepassmodel',
            name='Created_time',
            field=models.TimeField(default='20:21:07'),
        ),
        migrations.AlterField(
            model_name='workpermit',
            name='Created_time',
            field=models.TimeField(default='20:21:07'),
        ),
    ]
