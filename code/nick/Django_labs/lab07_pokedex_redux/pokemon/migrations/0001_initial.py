# Generated by Django 3.2 on 2021-08-03 01:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('image_front', models.URLField()),
                ('image_back', models.URLField()),
                ('caught_by', models.ManyToManyField(related_name='caught', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('pokemon', models.ManyToManyField(related_name='types', to='pokemon.Pokemon')),
            ],
        ),
    ]
