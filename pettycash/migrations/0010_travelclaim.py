# Generated by Django 4.2.8 on 2024-02-07 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0056_alter_checklistdetails_time_and_more'),
        ('pettycash', '0009_alter_expense_station_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TravelClaim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('days', models.DecimalField(decimal_places=0, max_digits=2)),
                ('justification', models.CharField(max_length=255)),
                ('accommodation', models.DecimalField(decimal_places=2, max_digits=8)),
                ('meals', models.DecimalField(decimal_places=2, max_digits=8)),
                ('transportation', models.DecimalField(decimal_places=2, max_digits=8)),
                ('miscellaneous', models.DecimalField(decimal_places=2, max_digits=8)),
                ('upload_bill', models.FileField(upload_to='travelclaimbills/')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.station')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
