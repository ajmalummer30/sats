# Generated by Django 4.2.8 on 2024-01-01 07:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pettycash', '0005_alter_expense_total_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='claimant',
            field=models.CharField(default='ajmal', max_length=100),
        ),
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
