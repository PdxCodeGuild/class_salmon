# Generated by Django 3.2.5 on 2021-07-27 19:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list', '0003_auto_20210727_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='groceryitem',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 27, 19, 16, 27, 990186, tzinfo=utc)),
        ),
    ]
