# Generated by Django 3.2.6 on 2021-08-24 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalapp', '0015_auto_20210823_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profile_pic',
            field=models.ImageField(blank=True, default='iitbhu.jpeg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='pic',
            field=models.ImageField(blank=True, default='iitbhu.jpeg', upload_to=''),
        ),
    ]