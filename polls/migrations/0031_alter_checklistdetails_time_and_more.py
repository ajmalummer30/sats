# Generated by Django 4.2.8 on 2024-01-10 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0030_alter_checklistdetails_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistdetails',
            name='time',
            field=models.TimeField(default='13:18:03'),
        ),
        migrations.AlterField(
            model_name='workpermit',
            name='Created_time',
            field=models.TimeField(default='13:18:03'),
        ),
    ]
