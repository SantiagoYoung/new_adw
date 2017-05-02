# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20161130_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='description',
            field=models.CharField(default=None, max_length=213, verbose_name='\u5546\u54c1\u63cf\u8ff0'),
        ),
        migrations.AddField(
            model_name='goods',
            name='price',
            field=models.FloatField(default=None, max_length=123, verbose_name='\u4ef7\u683c'),
        ),
        migrations.AlterField(
            model_name='bigtype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 1, 2, 57, 21, 575291, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='goods',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 1, 2, 57, 21, 576489, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='goods',
            name='picture',
            field=models.ImageField(default=None, upload_to=b'goods/', verbose_name='\u56fe\u7247'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='small_type',
            field=models.ForeignKey(related_name='goods', to='goods.SmallType'),
        ),
        migrations.AlterField(
            model_name='smalltype',
            name='big_type',
            field=models.ForeignKey(related_name='small', to='goods.BigType'),
        ),
        migrations.AlterField(
            model_name='smalltype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 1, 2, 57, 21, 575847, tzinfo=utc)),
        ),
    ]
