# Generated by Django 2.2.24 on 2021-07-27 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('url_short', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shortener',
            old_name='short_url',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='shortener',
            old_name='long_url',
            new_name='url',
        ),
    ]
