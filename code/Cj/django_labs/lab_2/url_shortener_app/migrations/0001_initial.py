# Generated by Django 3.2.5 on 2021-07-27 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('short_url', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField()),
            ],
        ),
    ]
