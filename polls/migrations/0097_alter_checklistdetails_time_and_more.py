# Generated by Django 4.2.8 on 2024-02-17 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0096_alter_checklistdetails_equipment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistdetails',
            name='time',
            field=models.TimeField(default='20:41:59'),
        ),
        migrations.AlterField(
            model_name='workpermit',
            name='Created_time',
            field=models.TimeField(default='20:41:59'),
        ),
        migrations.CreateModel(
            name='EquipmentSpecificQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Enter New question')),
                ('fueltype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.fuel')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.equipment')),
            ],
        ),
    ]
