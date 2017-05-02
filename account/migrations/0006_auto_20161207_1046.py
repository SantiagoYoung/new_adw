# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20161206_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='vip',
            name='phone',
            field=models.CharField(max_length=19, null=True, verbose_name='\u7535\u8bdd\u53f7\u7801', blank=True),
        ),
        migrations.AlterField(
            model_name='messageboard',
            name='creat_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 2, 46, 11, 255899, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='messagetype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 2, 46, 11, 255375, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='reply_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 2, 46, 11, 256468, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='join_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 2, 46, 11, 253927, tzinfo=utc)),
        ),
    ]
