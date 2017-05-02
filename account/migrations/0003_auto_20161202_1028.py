# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20161130_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageboard',
            name='creat_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 2, 2, 28, 42, 135696, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='messagetype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 2, 2, 28, 42, 135043, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='reply_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 2, 2, 28, 42, 136243, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='join_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 2, 2, 28, 42, 133603, tzinfo=utc)),
        ),
    ]
