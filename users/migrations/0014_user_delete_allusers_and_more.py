# Generated by Django 4.1.2 on 2022-11-08 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_assessmenttest_answer_1_assessmenttest_answer_2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, null=True)),
                ('specialist_id', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
                ('password1', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=400, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('province', models.CharField(max_length=100, null=True)),
                ('zipcode', models.CharField(max_length=10, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('category', models.CharField(choices=[('counselor', 'Counselor'), ('doctor', 'Doctor'), ('patient', 'Patient')], default='patient', max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='AllUsers',
        ),
        migrations.AddField(
            model_name='assessmenttest',
            name='assign_specialist_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='assessmenttest',
            name='state',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='assessmenttest',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
    ]