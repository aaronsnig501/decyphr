# Generated by Django 3.0.3 on 2020-05-13 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0002_language_short_code'),
        ('accounts', '0002_userprofile_language_preference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='language_preference',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='site_language_preference', to='languages.Language'),
        ),
    ]
