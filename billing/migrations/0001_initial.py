# Generated by Django 4.0.6 on 2022-07-23 10:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proveedor_name', models.CharField(max_length=50)),
                ('proveedor_location', models.CharField(max_length=50)),
                ('proveedor_phone', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=50)),
                ('date_init', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]