# Generated by Django 4.0.2 on 2022-05-21 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_mentorprocess'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorprocess',
            name='send_contract',
            field=models.BooleanField(default=False),
        ),
    ]