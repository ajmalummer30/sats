# Generated by Django 4.2.8 on 2024-05-16 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itassets', '0052_maintenancerequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenancerequest',
            name='Payment_Mode',
            field=models.CharField(choices=[('1', 'PO'), ('2', 'Cash')], default='1', max_length=20),
        ),
    ]
