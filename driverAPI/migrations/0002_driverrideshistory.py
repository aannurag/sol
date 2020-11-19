# Generated by Django 2.1.2 on 2018-10-23 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('passengerAPI', '0009_requestedcab'),
        ('driverAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverRidesHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_address', models.TextField()),
                ('destination_address', models.TextField()),
                ('booked_time', models.DateTimeField(auto_now_add=True)),
                ('distance_travelled', models.IntegerField()),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driverAPI.Driver')),
                ('passenger_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passengerAPI.Passenger')),
            ],
        ),
    ]