# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0011_auto_20161207_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='is_collected',
        ),
        migrations.AlterField(
            model_name='bigtype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 8, 22, 40, 319686, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='carouselfigure',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 8, 22, 40, 319054, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='goods',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 8, 22, 40, 322693, tzinfo=utc), verbose_name='\u53d1\u5e03\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_status',
            field=models.IntegerField(default=0, max_length=1, verbose_name='\u5546\u54c1\u5ba1\u6838\u72b6\u6001', choices=[(0, '\u5ba1\u6838\u672a\u901a\u8fc7'), (1, '\u5ba1\u6838\u4e2d'), (2, '\u5ba1\u6838\u901a\u8fc7')]),
        ),
        migrations.AlterField(
            model_name='goods',
            name='show_type',
            field=models.IntegerField(default=0, max_length=1, verbose_name='\u5546\u54c1\u5c55\u793a\u7c7b\u578b', choices=[(0, '\u4e0d\u5c55\u793a'), (1, '\u5c55\u793a')]),
        ),
        migrations.AlterField(
            model_name='goodscollection',
            name='collected_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 8, 22, 40, 324053, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='smalltype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 8, 22, 40, 320368, tzinfo=utc)),
        ),
    ]
