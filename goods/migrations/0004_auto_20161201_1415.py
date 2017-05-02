# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20161201_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='bigtype',
            name='english_name',
            field=models.CharField(default=None, max_length=123, verbose_name='\u82f1\u8bed\u540d'),
        ),
        migrations.AlterField(
            model_name='bigtype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 1, 6, 15, 5, 206472, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='goods',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 1, 6, 15, 5, 207770, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='smalltype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 1, 6, 15, 5, 207126, tzinfo=utc)),
        ),
    ]
