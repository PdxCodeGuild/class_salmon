# Generated by Django 2.2.24 on 2021-07-29 20:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20210729_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_posted',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 7, 29, 20, 46, 57, 845221, tzinfo=utc)),
        ),
    ]