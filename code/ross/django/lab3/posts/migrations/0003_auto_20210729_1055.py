# Generated by Django 2.2.24 on 2021-07-29 17:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_time_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_posted',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 7, 29, 17, 55, 24, 238264, tzinfo=utc)),
        ),
    ]
