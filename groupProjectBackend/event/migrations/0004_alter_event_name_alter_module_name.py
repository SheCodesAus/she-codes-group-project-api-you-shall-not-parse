# Generated by Django 4.0.2 on 2022-05-21 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_remove_eventmodulerole_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.SlugField(max_length=64),
        ),
        migrations.AlterField(
            model_name='module',
            name='name',
            field=models.SlugField(max_length=64),
        ),
    ]