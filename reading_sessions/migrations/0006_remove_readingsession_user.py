# Generated by Django 3.0.3 on 2020-06-18 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reading_sessions', '0005_readingsession_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readingsession',
            name='user',
        ),
    ]
