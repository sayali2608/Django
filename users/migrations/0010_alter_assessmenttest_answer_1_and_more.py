# Generated by Django 4.1.2 on 2022-11-06 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_assessmenttest_answer_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessmenttest',
            name='answer_1',
            field=models.CharField(choices=[('Not at all', 'Not at all'), ('Several Days', 'Several Days'), ('More than half the Days', 'More than half the Days'), ('Nearly everydays', 'Nearly everydays')], default='Not at all', max_length=200),
        ),
        migrations.AlterField(
            model_name='assessmenttest',
            name='answer_2',
            field=models.CharField(choices=[('Not at all', 'Not at all'), ('Several Days', 'Several Days'), ('More than half the Days', 'More than half the Days'), ('Nearly everydays', 'Nearly everydays')], max_length=200),
        ),
        migrations.AlterField(
            model_name='assessmenttest',
            name='answer_3',
            field=models.CharField(choices=[('Not at all', 'Not at all'), ('Several Days', 'Several Days'), ('More than half the Days', 'More than half the Days'), ('Nearly everydays', 'Nearly everydays')], max_length=200),
        ),
        migrations.AlterField(
            model_name='assessmenttest',
            name='answer_4',
            field=models.CharField(choices=[('Not at all', 'Not at all'), ('Several Days', 'Several Days'), ('More than half the Days', 'More than half the Days'), ('Nearly everydays', 'Nearly everydays')], max_length=200),
        ),
        migrations.AlterField(
            model_name='assessmenttest',
            name='answer_5',
            field=models.CharField(choices=[('Not at all', 'Not at all'), ('Several Days', 'Several Days'), ('More than half the Days', 'More than half the Days'), ('Nearly everydays', 'Nearly everydays')], max_length=200),
        ),
        migrations.AlterField(
            model_name='assessmenttest',
            name='answer_6',
            field=models.CharField(choices=[('Not at all', 'Not at all'), ('Several Days', 'Several Days'), ('More than half the Days', 'More than half the Days'), ('Nearly everydays', 'Nearly everydays')], max_length=200),
        ),
        migrations.AlterField(
            model_name='assessmenttest',
            name='answer_7',
            field=models.CharField(choices=[('Not at all', 'Not at all'), ('Several Days', 'Several Days'), ('More than half the Days', 'More than half the Days'), ('Nearly everydays', 'Nearly everydays')], max_length=200),
        ),
        migrations.AlterField(
            model_name='assessmenttest',
            name='answer_8',
            field=models.CharField(choices=[('Not at all', 'Not at all'), ('Several Days', 'Several Days'), ('More than half the Days', 'More than half the Days'), ('Nearly everydays', 'Nearly everydays')], max_length=200),
        ),
        migrations.AlterField(
            model_name='assessmenttest',
            name='answer_9',
            field=models.CharField(choices=[('Not at all', 'Not at all'), ('Several Days', 'Several Days'), ('More than half the Days', 'More than half the Days'), ('Nearly everydays', 'Nearly everydays')], max_length=200),
        ),
    ]
