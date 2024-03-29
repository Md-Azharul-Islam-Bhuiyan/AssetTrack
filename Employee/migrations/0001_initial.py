# Generated by Django 5.0 on 2024-03-15 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=30)),
                ('phone_no', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('Address', models.TextField()),
            ],
        ),
    ]
