# Generated by Django 4.2.8 on 2024-02-04 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itassets', '0017_alter_itassetallocation_allocation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='it_prodcuts',
            name='allocation_status',
            field=models.ForeignKey(default=2, max_length=20, on_delete=django.db.models.deletion.CASCADE, to='itassets.allocation_status'),
        ),
    ]
