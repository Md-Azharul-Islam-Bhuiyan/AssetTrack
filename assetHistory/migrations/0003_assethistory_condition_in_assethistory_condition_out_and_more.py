# Generated by Django 5.0 on 2024-03-16 08:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0003_employeemodel_company'),
        ('assetHistory', '0002_alter_assethistory_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='assethistory',
            name='condition_in',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='assethistory',
            name='condition_out',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='assethistory',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='assethistory',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Employee.employeemodel'),
        ),
    ]
