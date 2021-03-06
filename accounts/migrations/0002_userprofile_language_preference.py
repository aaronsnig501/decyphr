# Generated by Django 3.0.3 on 2020-05-02 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0002_language_short_code'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='language_preference',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='site_language_preference', to='languages.Language'),
            preserve_default=False,
        ),
    ]
