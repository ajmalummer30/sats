# Generated by Django 4.2.8 on 2024-02-17 10:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pettycash', '0034_alter_expense_date_alter_travelclaim_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='travelclaim',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
