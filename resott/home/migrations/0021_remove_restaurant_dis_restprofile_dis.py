# Generated by Django 4.0.1 on 2022-06-02 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_restaurant_dis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='dis',
        ),
        migrations.AddField(
            model_name='restprofile',
            name='dis',
            field=models.IntegerField(default=0),
        ),
    ]
