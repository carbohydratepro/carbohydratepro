# Generated by Django 3.2 on 2024-10-29 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_sensordata'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensordata',
            name='illuminance',
            field=models.FloatField(default=None),
        ),
    ]
