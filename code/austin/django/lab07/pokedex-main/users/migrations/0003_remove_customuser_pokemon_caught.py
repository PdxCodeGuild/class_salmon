# Generated by Django 3.2.7 on 2021-09-10 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_pokemon_caught'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='pokemon_caught',
        ),
    ]
