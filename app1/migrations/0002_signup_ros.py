# Generated by Django 4.0.2 on 2022-02-27 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='RoS',
            field=models.BooleanField(default=False),
        ),
    ]
