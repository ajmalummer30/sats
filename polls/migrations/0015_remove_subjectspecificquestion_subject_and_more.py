# Generated by Django 4.2.8 on 2023-12-23 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_subjectspecificquestion_fueltype_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjectspecificquestion',
            name='subject',
        ),
        migrations.AlterField(
            model_name='checklistdetails',
            name='time',
            field=models.TimeField(default='10:23:10'),
        ),
        migrations.AlterField(
            model_name='subjectspecificquestion',
            name='fueltype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.fuel'),
        ),
    ]
