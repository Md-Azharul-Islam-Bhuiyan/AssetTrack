# Generated by Django 5.0 on 2024-03-16 09:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0001_initial'),
        ('Employee', '0004_alter_employeemodel_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Company.companymodel'),
        ),
    ]
