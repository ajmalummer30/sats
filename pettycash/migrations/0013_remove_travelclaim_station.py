# Generated by Django 4.2.8 on 2024-02-07 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pettycash', '0012_alter_travelclaim_accommodation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travelclaim',
            name='station',
        ),
    ]
