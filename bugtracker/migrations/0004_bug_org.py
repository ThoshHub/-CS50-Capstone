# Generated by Django 3.1.5 on 2021-02-01 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker', '0003_auto_20210131_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='org',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='error', to='bugtracker.organization'),
        ),
    ]