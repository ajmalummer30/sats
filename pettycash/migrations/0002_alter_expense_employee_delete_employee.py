# Generated by Django 4.2.8 on 2023-12-25 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pettycash', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
