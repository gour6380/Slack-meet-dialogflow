# Generated by Django 3.2.9 on 2021-11-29 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slackuser',
            name='is_bot',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
