# Generated by Django 3.2.5 on 2021-07-27 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('short_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shortness',
            name='item_id',
        ),
    ]
