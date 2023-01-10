# Generated by Django 4.1.2 on 2022-10-30 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_allusers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allusers',
            name='city',
        ),
        migrations.RemoveField(
            model_name='allusers',
            name='country',
        ),
        migrations.RemoveField(
            model_name='allusers',
            name='province',
        ),
        migrations.RemoveField(
            model_name='allusers',
            name='street',
        ),
        migrations.RemoveField(
            model_name='allusers',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='allusers',
            name='address',
            field=models.CharField(max_length=400, null=True),
        ),
    ]