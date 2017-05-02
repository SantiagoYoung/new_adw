# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0006_auto_20161201_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='collected_number',
            field=models.IntegerField(default=12, null=True, verbose_name='\u6536\u85cf\u6570', blank=True),
        ),
        migrations.AddField(
            model_name='goods',
            name='collector',
            field=models.ManyToManyField(related_name='goods_collector', null=True, verbose_name='\u6536\u85cf\u8005', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='goods',
            name='colors',
            field=models.CharField(default='\u65e0', max_length=123, verbose_name='\u5546\u54c1\u989c\u8272'),
        ),
        migrations.AddField(
            model_name='goods',
            name='custom_pattern',
            field=models.BooleanField(default=False, verbose_name='\u5b9a\u5236\u56fe\u6848'),
        ),
        migrations.AddField(
            model_name='goods',
            name='custom_size',
            field=models.BooleanField(default=False, verbose_name='\u5b9a\u5236\u5c3a\u5bf8'),
        ),
        migrations.AddField(
            model_name='goods',
            name='custom_style',
            field=models.BooleanField(default=False, verbose_name='\u5b9a\u5236\u6b3e\u5f0f'),
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_status',
            field=models.CharField(default=0, max_length=1, verbose_name='\u5546\u54c1\u5ba1\u6838\u72b6\u6001', choices=[(0, '\u5ba1\u6838\u672a\u901a\u8fc7'), (1, '\u5ba1\u6838\u4e2d'), (2, '\u5ba1\u6838\u901a\u8fc7')]),
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_stock',
            field=models.IntegerField(default=12, null=True, verbose_name='\u5e93\u5b58', blank=True),
        ),
        migrations.AddField(
            model_name='goods',
            name='is_collected',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u88ab\u6536\u85cf'),
        ),
        migrations.AddField(
            model_name='goods',
            name='provide_design',
            field=models.BooleanField(default=False, verbose_name='\u63d0\u4f9b\u8bbe\u8ba1'),
        ),
        migrations.AddField(
            model_name='goods',
            name='provide_produce',
            field=models.BooleanField(default=False, verbose_name='\u63d0\u4f9b\u5236\u4f5c'),
        ),
        migrations.AddField(
            model_name='goods',
            name='seller',
            field=models.ForeignKey(related_name='goods_seller', verbose_name='\u5356\u5bb6', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='goods',
            name='show_type',
            field=models.CharField(default=0, max_length=1, verbose_name='\u5546\u54c1\u5c55\u793a\u7c7b\u578b', choices=[(0, '\u4e0d\u5c55\u793a'), (1, '\u5c55\u793a')]),
        ),
        migrations.AlterField(
            model_name='bigtype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 2, 2, 28, 42, 138901, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='carouselfigure',
            name='create_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 12, 2, 2, 28, 42, 138195, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='goods',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 2, 2, 28, 42, 140668, tzinfo=utc), verbose_name='\u53d1\u5e03\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='smalltype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 2, 2, 28, 42, 139596, tzinfo=utc)),
        ),
    ]
