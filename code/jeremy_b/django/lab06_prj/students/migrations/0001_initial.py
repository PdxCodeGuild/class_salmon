# Generated by Django 3.2.7 on 2021-09-03 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('cohort', models.CharField(max_length=100)),
                ('fav_topic', models.CharField(max_length=100)),
                ('fav_teach', models.CharField(max_length=100)),
                ('capstone_url', models.URLField()),
            ],
        ),
    ]
