# Generated by Django 4.1.2 on 2022-10-28 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profile_location_profile_birthdate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birthdate',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='province',
        ),
    ]
