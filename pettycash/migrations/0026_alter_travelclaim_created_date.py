# Generated by Django 4.2.8 on 2024-02-13 14:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pettycash', '0025_expense_approved_date_alter_travelclaim_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelclaim',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 13, 14, 2, 49, 834511, tzinfo=datetime.timezone.utc)),
        ),
    ]
