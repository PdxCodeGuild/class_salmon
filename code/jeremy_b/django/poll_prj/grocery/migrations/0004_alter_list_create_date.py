# Generated by Django 3.2.5 on 2021-07-22 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0003_alter_list_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='create_date',
            field=models.DateTimeField(),
        ),
    ]
