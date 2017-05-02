# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20161202_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageboard',
            name='creat_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 6, 7, 10, 19, 756168, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='messagetype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 6, 7, 10, 19, 755659, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='reply_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 6, 7, 10, 19, 756709, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='join_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 6, 7, 10, 19, 754284, tzinfo=utc)),
        ),
    ]
