# Generated by Django 3.2.9 on 2021-11-29 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='slackuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slackuseID', models.CharField(max_length=50)),
                ('teamID', models.CharField(max_length=50)),
                ('real_name', models.CharField(max_length=500)),
                ('is_admin', models.IntegerField()),
                ('is_owner', models.IntegerField()),
                ('is_primary_owner', models.IntegerField()),
                ('is_restricted', models.IntegerField()),
                ('is_ultra_restricted', models.IntegerField()),
                ('is_deleted', models.IntegerField()),
            ],
        ),
    ]