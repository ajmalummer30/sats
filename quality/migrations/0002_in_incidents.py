# Generated by Django 4.2.8 on 2024-02-21 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_customuser_station_name'),
        ('quality', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='In_Incidents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=100)),
                ('date_of_occurance', models.DateField()),
                ('time_of_occurance', models.TimeField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quality.in_category')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.station')),
                ('surface_condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quality.in_surfacecondition')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quality.in_incidenttype')),
                ('visibility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quality.in_visibility')),
                ('whether_condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quality.whethercondition')),
            ],
        ),
    ]
