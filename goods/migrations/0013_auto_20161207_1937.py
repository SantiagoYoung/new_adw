# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0012_auto_20161207_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='collecters',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, verbose_name='\u6536\u85cf\u8005', blank=True),
        ),
        migrations.AlterField(
            model_name='bigtype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 11, 37, 5, 519492, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='carouselfigure',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 11, 37, 5, 518564, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='goods',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 11, 37, 5, 521671, tzinfo=utc), verbose_name='\u53d1\u5e03\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='goodscollection',
            name='collected_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 11, 37, 5, 523998, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='smalltype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 11, 37, 5, 520349, tzinfo=utc)),
        ),
    ]
