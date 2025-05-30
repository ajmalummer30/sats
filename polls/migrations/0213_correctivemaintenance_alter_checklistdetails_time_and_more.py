# Generated by Django 4.2.8 on 2024-06-03 11:15

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_alter_customuser_employee_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0212_fa_category_fa_contract_alter_checklistdetails_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorrectiveMaintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Scope_of_Work', models.CharField(max_length=256, null=True)),
                ('purchase_order', models.CharField(max_length=100, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('uploaded_at', models.DateField(default=django.utils.timezone.now)),
                ('cm_datetime', models.DateTimeField(auto_now_add=True)),
                ('Created_By', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Fa_CM_category', to='polls.fa_category')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.fa_contract')),
                ('contractor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Fa_CM_contractor', to='polls.contractor')),
                ('station_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.station')),
                ('subcategory', models.ManyToManyField(null=True, to='polls.fa_subcategory')),
            ],
        ),
        migrations.AlterField(
            model_name='checklistdetails',
            name='time',
            field=models.TimeField(default='14:15:03'),
        ),
        migrations.AlterField(
            model_name='workpermit',
            name='Created_time',
            field=models.TimeField(default=datetime.datetime(2024, 6, 3, 11, 15, 3, 484790, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Workorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type_of_work', models.IntegerField(choices=[(1, 'PM'), (2, 'CM'), (3, 'OTHER')])),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('Created_By', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('station_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.station')),
            ],
        ),
        migrations.CreateModel(
            name='PreventiveMaintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateField(default=django.utils.timezone.now)),
                ('pm_datetime', models.DateTimeField(auto_now_add=True)),
                ('details', models.CharField(max_length=256)),
                ('Created_By', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.fa_contract')),
                ('station_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.station')),
                ('work_order', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='preventivemaintenance', to='polls.workorder')),
            ],
        ),
        migrations.CreateModel(
            name='PM_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('pm_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PM_comments', to='polls.preventivemaintenance')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fa_PM_ContractFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='contracts/pmattachment', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('filename', models.CharField(max_length=255, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('Created_By', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('pm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Fa_PM_ContractFile', to='polls.preventivemaintenance')),
            ],
        ),
        migrations.CreateModel(
            name='Fa_CM_ContractFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='contracts/cmattachment', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('filename', models.CharField(max_length=255, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('Created_By', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('cm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Fa_CM_ContractFile', to='polls.correctivemaintenance')),
            ],
        ),
        migrations.AddField(
            model_name='correctivemaintenance',
            name='work_order',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='correctivemaintenance', to='polls.workorder'),
        ),
        migrations.CreateModel(
            name='CM_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('cm_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CM_comments', to='polls.correctivemaintenance')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
