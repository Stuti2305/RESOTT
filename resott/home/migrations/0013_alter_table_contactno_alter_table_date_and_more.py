# Generated by Django 4.0.1 on 2022-05-16 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='contactno',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='table',
            name='date',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='table',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='table',
            name='time',
            field=models.CharField(max_length=200),
        ),
    ]
