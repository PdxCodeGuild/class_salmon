# Generated by Django 3.2.5 on 2021-07-26 18:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubmittedUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_description', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2021, 7, 26, 18, 31, 13, 746710, tzinfo=utc))),
            ],
        ),
    ]
