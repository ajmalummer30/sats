# Generated by Django 4.2.8 on 2024-02-03 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itassets', '0014_it_prodcuts_current_allocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itassetallocation',
            name='allocation_date',
            field=models.DateTimeField(),
        ),
    ]
