# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageboard',
            name='creat_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 30, 8, 2, 43, 799479, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='messagetype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 30, 8, 2, 43, 798840, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='reply',
            name='reply_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 30, 8, 2, 43, 800051, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='join_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 30, 8, 2, 43, 797498, tzinfo=utc)),
        ),
    ]
