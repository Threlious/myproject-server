# Generated by Django 3.2.12 on 2022-04-03 09:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 5, 9, 19, 4, 149083, tzinfo=utc), null=True),
        ),
    ]
