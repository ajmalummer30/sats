# Generated by Django 4.2.8 on 2024-02-01 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_customuser_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='employee_id',
            field=models.CharField(default='SSA10010019', max_length=20),
        ),
    ]
