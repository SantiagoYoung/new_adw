# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0009_auto_20161206_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bigtype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 6, 11, 27, 31, 711889, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='carouselfigure',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 6, 11, 27, 31, 711210, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='goods',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 6, 11, 27, 31, 713709, tzinfo=utc), verbose_name='\u53d1\u5e03\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='goodscollection',
            name='collected_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 6, 11, 27, 31, 715093, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='smalltype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 6, 11, 27, 31, 712742, tzinfo=utc)),
        ),
    ]
