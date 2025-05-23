# Generated by Django 4.2.8 on 2024-02-17 19:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pettycash', '0041_alter_travelclaim_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelclaim',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='travelclaim',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
