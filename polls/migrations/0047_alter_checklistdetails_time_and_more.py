# Generated by Django 4.2.8 on 2024-02-01 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0046_alter_checklistdetails_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistdetails',
            name='time',
            field=models.TimeField(default='15:29:26'),
        ),
        migrations.AlterField(
            model_name='workpermit',
            name='Created_time',
            field=models.TimeField(default='15:29:26'),
        ),
    ]
