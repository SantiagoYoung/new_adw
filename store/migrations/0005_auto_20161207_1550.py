# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20161206_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sotrecollection',
            name='collected_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 7, 50, 36, 195082, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='sotrecollection',
            name='store',
            field=models.OneToOneField(null=True, blank=True, to='store.Store'),
        ),
        migrations.AlterField(
            model_name='sotrecollection',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, verbose_name='\u6536\u85cf\u8005', blank=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='company_form',
            field=models.IntegerField(default=0, max_length=2, choices=[(0, '\u516c\u53f8'), (1, '\u4e2a\u4eba')]),
        ),
        migrations.AlterField(
            model_name='store',
            name='store_status',
            field=models.IntegerField(default=3, max_length=3, choices=[(1, '\u5ba1\u6838\u4e2d'), (2, '\u5ba1\u6838\u901a\u8fc7'), (3, '\u5ba1\u6838\u672a\u901a\u8fc7')]),
        ),
        migrations.AlterField(
            model_name='store',
            name='store_style',
            field=models.IntegerField(default=0, max_length=4, choices=[(0, '\u5236\u4f5c(\u63d0\u4f9b\u6750\u6599)'), (1, '\u8bbe\u8ba1'), (2, '\u79c1\u4eba\u8ba2\u5236'), (3, '\u5de5\u88c5\u5b9a\u5236')]),
        ),
    ]
