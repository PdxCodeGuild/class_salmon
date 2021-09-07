# Generated by Django 3.2.7 on 2021-09-07 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_short', '0003_alter_shortener_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortener',
            name='code',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='shortener',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
