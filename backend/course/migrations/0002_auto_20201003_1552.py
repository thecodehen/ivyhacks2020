# Generated by Django 3.1.1 on 2020-10-03 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='brief_problem_statement',
        ),
        migrations.AddField(
            model_name='problem',
            name='description',
            field=models.CharField(default='', max_length=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='problem',
            name='title',
            field=models.CharField(default='', max_length=10000),
            preserve_default=False,
        ),
    ]