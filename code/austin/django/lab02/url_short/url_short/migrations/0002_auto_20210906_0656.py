# Generated by Django 3.2.7 on 2021-09-06 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_short', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shortener',
            name='date_created',
        ),
        migrations.AlterField(
            model_name='shortener',
            name='code',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
