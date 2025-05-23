# Generated by Django 4.2.8 on 2024-06-03 10:18

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0016_alter_customuser_employee_id'),
        ('polls', '0211_alter_checklistdetails_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fa_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fa_Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_reference_number', models.CharField(max_length=100, unique=True)),
                ('Account_Manager', models.CharField(max_length=256, null=True)),
                ('Contact_Details', models.CharField(max_length=256, null=True)),
                ('Email_ID', models.EmailField(max_length=254, null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('no_of_pm_visits', models.IntegerField(null=True)),
                ('frequency', models.IntegerField(choices=[(1, 'Monthly'), (2, 'Quarterly')], null=True)),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('PO_Number', models.CharField(max_length=256, null=True)),
                ('PO_copy', models.FileField(blank=True, null=True, upload_to='contracts/po/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('contract_copy', models.FileField(blank=True, null=True, upload_to='contracts/contractscopy/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('Created_By', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Fa_category', to='polls.fa_category')),
                ('contractor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='polls.contractor')),
                ('station_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.station')),
            ],
        ),
        migrations.AlterField(
            model_name='checklistdetails',
            name='time',
            field=models.TimeField(default='13:18:30'),
        ),
        migrations.AlterField(
            model_name='workpermit',
            name='Created_time',
            field=models.TimeField(default=datetime.datetime(2024, 6, 3, 10, 18, 30, 359001, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Fa_SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='polls.fa_category')),
            ],
        ),
        migrations.CreateModel(
            name='Fa_ContractFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='contracts/common/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('filename', models.CharField(max_length=255, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('Created_By', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Fa_ContractFile', to='polls.fa_contract')),
            ],
        ),
        migrations.AddField(
            model_name='fa_contract',
            name='subcategory',
            field=models.ManyToManyField(to='polls.fa_subcategory'),
        ),
    ]
