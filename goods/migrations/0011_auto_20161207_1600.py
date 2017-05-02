# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20161207_1600'),
        ('goods', '0010_auto_20161206_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='store',
            field=models.ForeignKey(verbose_name='\u5e97\u94fa', blank=True, to='store.Store', null=True),
        ),
        migrations.AlterField(
            model_name='bigtype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 8, 0, 25, 545814, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='carouselfigure',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 8, 0, 25, 545086, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='goods',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 8, 0, 25, 549129, tzinfo=utc), verbose_name='\u53d1\u5e03\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='goodscollection',
            name='collected_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 8, 0, 25, 550599, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='smalltype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 8, 0, 25, 546549, tzinfo=utc)),
        ),
    ]
