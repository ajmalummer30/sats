# Generated by Django 4.2.8 on 2024-10-04 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quality', '0016_employeesinvolved_driver_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
    ]
