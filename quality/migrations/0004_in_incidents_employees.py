# Generated by Django 4.2.8 on 2024-02-21 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quality', '0003_employeesinvolved'),
    ]

    operations = [
        migrations.AddField(
            model_name='in_incidents',
            name='employees',
            field=models.ManyToManyField(related_name='incidents', to='quality.employeesinvolved'),
        ),
    ]
