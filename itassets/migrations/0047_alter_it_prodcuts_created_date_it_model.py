# Generated by Django 4.2.8 on 2024-05-07 08:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itassets', '0046_it_prodcuts_location_it_prodcuts_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='it_prodcuts',
            name='created_date',
            field=models.DateField(default=datetime.date(2024, 5, 7)),
        ),
        migrations.CreateModel(
            name='It_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=100)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itassets.it_brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itassets.it_category')),
            ],
        ),
    ]
