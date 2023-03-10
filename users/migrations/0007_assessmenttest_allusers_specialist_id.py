# Generated by Django 4.1.2 on 2022-10-30 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_allusers_category_allusers_password1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssessmentTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('answer_1', models.CharField(max_length=200)),
                ('answer_2', models.CharField(max_length=200)),
                ('answer_3', models.CharField(max_length=200)),
                ('answer_4', models.CharField(max_length=200)),
                ('answer_5', models.CharField(max_length=200)),
                ('answer_6', models.CharField(max_length=200)),
                ('answer_7', models.CharField(max_length=200)),
                ('answer_8', models.CharField(max_length=200)),
                ('answer_9', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='allusers',
            name='specialist_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
