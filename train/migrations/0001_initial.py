# Generated by Django 5.0 on 2024-02-09 07:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=14)),
                ('nid', models.CharField(max_length=20)),
                ('train', models.CharField(max_length=50)),
                ('train_id', models.CharField(max_length=20)),
                ('start_station', models.CharField(max_length=50)),
                ('end_station', models.CharField(max_length=50)),
                ('fare', models.DecimalField(decimal_places=2, max_digits=12)),
                ('departure_time', models.CharField(max_length=20)),
                ('seat_number', models.CharField(max_length=20)),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('journey_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_no', models.CharField(max_length=10)),
                ('is_booked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=55, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_name', models.CharField(max_length=50, unique=True)),
                ('train_id', models.CharField(max_length=20, unique=True)),
                ('departure_time', models.CharField(choices=[('08:00 AM', '08:00 AM'), ('09:00 AM', '09:00 AM'), ('011:00 AM', '11:00 AM'), ('01:00 PM', '01:00 PM'), ('03:00 PM', '03:00 PM'), ('05:00 PM', '05:00 PM'), ('08:00 PM', '08:00 PM'), ('11:00 PM', '11:00 PM')], max_length=20)),
                ('seats_available', models.PositiveIntegerField()),
                ('start_station', models.CharField(max_length=50)),
                ('end_station', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('all_seats', models.ManyToManyField(to='train.seat')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='train.train')),
            ],
        ),
    ]
