# Generated by Django 3.2.6 on 2021-08-18 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalapp', '0013_alter_person_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profile_pic',
            field=models.ImageField(default='static/images/iitbhu.png', upload_to=''),
        ),
    ]
