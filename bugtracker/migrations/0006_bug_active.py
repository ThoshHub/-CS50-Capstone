# Generated by Django 3.1.5 on 2021-02-28 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker', '0005_auto_20210224_0507'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='active',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
