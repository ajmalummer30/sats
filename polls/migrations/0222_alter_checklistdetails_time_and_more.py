# Generated by Django 4.2.8 on 2024-06-04 08:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_alter_customuser_employee_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0221_alter_checklistdetails_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistdetails',
            name='time',
            field=models.TimeField(default='11:25:08'),
        ),
        migrations.AlterField(
            model_name='fa_contract',
            name='Account_Manager',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='fa_contract',
            name='Contact_Details',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='fa_contract',
            name='Created_By',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fa_contract',
            name='Email_ID',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='fa_contract',
            name='PO_Number',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='fa_contract',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='fa_contract',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Fa_category', to='polls.fa_category'),
        ),
        migrations.AlterField(
            model_name='fa_contract',
            name='contractor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='polls.contractor'),
        ),
        migrations.AlterField(
            model_name='fa_contract',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='fa_contract',
            name='frequency',
            field=models.IntegerField(choices=[(1, 'Monthly'), (2, 'Quarterly'), (3, 'Every 2 months'), (4, 'Every 4 months')], null=True),
        ),
        migrations.AlterField(
            model_name='fa_contract',
            name='no_of_pm_visits',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='fa_contract',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='fa_contract',
            name='station_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.station'),
        ),
        migrations.AlterField(
            model_name='fa_contract',
            name='subcategory',
            field=models.ManyToManyField(null=True, to='polls.fa_subcategory'),
        ),
        migrations.AlterField(
            model_name='workpermit',
            name='Created_time',
            field=models.TimeField(default=datetime.datetime(2024, 6, 4, 8, 25, 8, 655311, tzinfo=datetime.timezone.utc)),
        ),
    ]
