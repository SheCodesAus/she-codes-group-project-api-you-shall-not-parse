# Generated by Django 4.0.2 on 2022-05-31 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.SlugField(max_length=64)),
                ('description', models.TextField()),
                ('image', models.URLField(null=True)),
                ('published', models.BooleanField(default=False)),
                ('signup_opens', models.DateTimeField()),
                ('signup_closes', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventModuleRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('gift_back', models.BooleanField(default=False)),
                ('sign_up', models.BooleanField(default=False)),
                ('confirmation', models.BooleanField(default=False)),
                ('send_contract', models.BooleanField(default=False)),
                ('received_contract', models.BooleanField(default=False)),
                ('calendar_invites', models.BooleanField(default=False)),
                ('onboarding', models.BooleanField(default=False)),
                ('mentoring', models.BooleanField(default=False)),
                ('invoice_sent', models.BooleanField(default=False)),
                ('paid', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.SlugField(max_length=64)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.SlugField(max_length=64)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
