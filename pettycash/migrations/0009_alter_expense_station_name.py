# Generated by Django 4.2.8 on 2024-01-07 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0026_alter_checklistdetails_time_workpermit'),
        ('pettycash', '0008_expense_station_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='station_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.station'),
        ),
    ]
