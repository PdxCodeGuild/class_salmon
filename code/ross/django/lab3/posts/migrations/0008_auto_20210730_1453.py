# Generated by Django 2.2.24 on 2021-07-30 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20210729_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_posted',
            field=models.DateTimeField(auto_now=True),
        ),
    ]