# Generated by Django 4.2.8 on 2023-12-09 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
