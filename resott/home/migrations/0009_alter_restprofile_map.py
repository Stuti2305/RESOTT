# Generated by Django 4.0.1 on 2022-05-10 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_restprofile_map'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restprofile',
            name='map',
            field=models.URLField(default='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d227822.55035627162!2d80.8024271802209!3d26.84862299412667!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x399bfd991f32b16b%3A0x93ccba8909978be7!2sLucknow%2C%20Uttar%20Pradesh!5e0!3m2!1sen!2sin!4v1652175194751!5m2!1sen!2sin'),
        ),
    ]
