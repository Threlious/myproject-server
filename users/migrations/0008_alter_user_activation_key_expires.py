# Generated by Django 3.2.12 on 2022-04-03 11:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20220403_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 5, 11, 5, 27, 458456, tzinfo=utc), null=True),
        ),
    ]
