# Generated by Django 3.2.12 on 2022-04-02 11:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220402_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 4, 11, 4, 47, 418777, tzinfo=utc), null=True),
        ),
    ]
