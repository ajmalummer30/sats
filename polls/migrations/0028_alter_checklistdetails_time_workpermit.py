# Generated by Django 4.2.8 on 2024-01-07 13:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0027_alter_checklistdetails_time_delete_workpermit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistdetails',
            name='time',
            field=models.TimeField(default='16:37:12'),
        ),
        migrations.CreateModel(
            name='Workpermit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_date', models.DateField(default=datetime.date.today)),
                ('Created_time', models.TimeField(default='16:37:12')),
                ('Contractor_Name', models.CharField(max_length=100)),
                ('Staff_in_charge', models.CharField(max_length=100)),
                ('Phone_number', models.CharField(max_length=10)),
                ('Iqama_number', models.CharField(max_length=10)),
                ('Employee_Count', models.IntegerField()),
                ('Description', models.TextField()),
                ('Additional_notes', models.TextField()),
                ('Tools', models.TextField()),
                ('station_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.station')),
            ],
        ),
    ]
