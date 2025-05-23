# Generated by Django 4.2.8 on 2024-05-18 14:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itassets', '0062_alter_maintenancerequest_it_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenancerequest',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='itassets/maint_requests/'),
        ),
        migrations.AlterField(
            model_name='it_prodcuts',
            name='created_date',
            field=models.DateField(default=datetime.date(2024, 5, 18)),
        ),
        migrations.AlterField(
            model_name='maintenancerequest',
            name='Payment_Mode',
            field=models.CharField(blank=True, choices=[('1', 'PO'), ('2', 'Cash'), ('3', 'NA')], max_length=20, null=True),
        ),
    ]
