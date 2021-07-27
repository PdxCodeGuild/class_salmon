# Generated by Django 3.2.5 on 2021-07-26 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shortness',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.PositiveSmallIntegerField()),
                ('long_url', models.URLField(max_length=300)),
                ('short_url', models.CharField(max_length=50)),
            ],
        ),
    ]
