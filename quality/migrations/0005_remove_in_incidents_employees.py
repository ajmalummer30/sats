# Generated by Django 4.2.8 on 2024-02-21 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quality', '0004_in_incidents_employees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='in_incidents',
            name='employees',
        ),
    ]
