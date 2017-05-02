# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20161206_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageboard',
            name='creat_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 6, 11, 27, 31, 709897, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='messagetype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 6, 11, 27, 31, 709385, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='reply_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 6, 11, 27, 31, 710451, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='join_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 6, 11, 27, 31, 708015, tzinfo=utc)),
        ),
    ]
