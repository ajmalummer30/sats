# Generated by Django 4.2.8 on 2024-05-16 07:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itassets', '0048_it_prodcuts_device_model_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='it_prodcuts',
            name='created_date',
            field=models.DateField(default=datetime.date(2024, 5, 16)),
        ),
        migrations.CreateModel(
            name='It_Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imei', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('Itproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobile_phone', to='itassets.it_prodcuts')),
            ],
        ),
        migrations.CreateModel(
            name='CCTV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('it_product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cctv', to='itassets.it_prodcuts')),
            ],
        ),
    ]
