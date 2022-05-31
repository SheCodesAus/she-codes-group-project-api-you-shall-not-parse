# Generated by Django 4.0.2 on 2022-05-27 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_eventmodulerole_calendar_invites_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventmodulerole',
            name='event',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_name', to='event.event'),
        ),
    ]
