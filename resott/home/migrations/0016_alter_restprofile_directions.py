# Generated by Django 4.0.1 on 2022-05-17 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_restprofile_about_alter_restprofile_directions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restprofile',
            name='directions',
            field=models.CharField(max_length=10000),
        ),
    ]
