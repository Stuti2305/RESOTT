# Generated by Django 4.0.1 on 2022-05-09 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='status_full',
            field=models.BooleanField(default=False),
        ),
    ]
