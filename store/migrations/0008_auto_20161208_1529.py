# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0007_auto_20161207_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='collecter',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, verbose_name='\u6536\u85cf\u8005', blank=True),
        ),
        migrations.AlterField(
            model_name='sotrecollection',
            name='collected_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 8, 7, 29, 38, 328965, tzinfo=utc)),
        ),
    ]
