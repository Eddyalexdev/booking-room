# Generated by Django 4.0.6 on 2022-07-23 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_booking_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='state',
            field=models.CharField(choices=[('1', 'Pendiente'), ('2', 'Pagado'), ('3', 'Eliminado')], max_length=50, verbose_name='State'),
        ),
    ]
