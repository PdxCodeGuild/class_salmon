# Generated by Django 3.2.5 on 2021-07-27 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0003_clickdata_clicks_to_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clickdata',
            name='clicks_to_date',
        ),
        migrations.AddField(
            model_name='urlshortener',
            name='clicks',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
