# Generated by Django 4.2.8 on 2024-02-16 20:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0078_alter_checklistdetails_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectspecificquestion',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.subject'),
        ),
        migrations.AlterField(
            model_name='checklistdetails',
            name='equipment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.subject'),
        ),
        migrations.AlterField(
            model_name='checklistdetails',
            name='time',
            field=models.TimeField(default='23:33:04'),
        ),
        migrations.AlterField(
            model_name='checklistdetails',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='genquestionresponse',
            name='checklistid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.checklistdetails'),
        ),
        migrations.AlterField(
            model_name='genquestionresponse',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.generalquestion'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='fueltype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.fuel'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='station_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.station'),
        ),
        migrations.AlterField(
            model_name='subjectspecificquestion',
            name='fueltype',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.fuel'),
        ),
        migrations.AlterField(
            model_name='subquestionresponse',
            name='checklistid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.checklistdetails'),
        ),
        migrations.AlterField(
            model_name='subquestionresponse',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.subjectspecificquestion'),
        ),
        migrations.AlterField(
            model_name='workpermit',
            name='Created_time',
            field=models.TimeField(default='23:33:04'),
        ),
        migrations.AlterField(
            model_name='workpermit',
            name='station_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.station'),
        ),
    ]
