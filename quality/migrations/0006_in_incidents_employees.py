# Generated by Django 4.2.8 on 2024-02-21 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quality', '0005_remove_in_incidents_employees'),
    ]

    operations = [
        migrations.AddField(
            model_name='in_incidents',
            name='employees',
            field=models.ManyToManyField(related_name='incidents', to='quality.employeesinvolved'),
        ),
    ]
