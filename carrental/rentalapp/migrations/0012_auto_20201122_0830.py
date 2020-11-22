# Generated by Django 3.1.2 on 2020-11-22 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalapp', '0011_person_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='availability_end_date',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='availability_start_date',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='drop_address',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='per_day_cost',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='per_km_cost',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='pickup_address',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='pic',
            field=models.ImageField(default='images/iitbhu.png', upload_to='images'),
        ),
    ]