# Generated by Django 4.2.8 on 2024-04-05 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0160_gatepassmodel_user_alter_checklistdetails_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistdetails',
            name='time',
            field=models.TimeField(default='15:01:54'),
        ),
        migrations.AlterField(
            model_name='gatepassmodel',
            name='Created_time',
            field=models.TimeField(default='15:01:54'),
        ),
        migrations.AlterField(
            model_name='gatepassmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workpermit',
            name='Created_time',
            field=models.TimeField(default='15:01:54'),
        ),
    ]
