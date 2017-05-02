# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': '\u5546\u54c1', 'verbose_name_plural': '\u5546\u54c1'},
        ),
        migrations.AddField(
            model_name='goods',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 30, 13, 23, 49, 34359, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='goods',
            name='picture',
            field=models.ImageField(default=None, upload_to=b'/goods', verbose_name='\u56fe\u7247'),
        ),
        migrations.AlterField(
            model_name='bigtype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 30, 13, 23, 49, 33172, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='goods',
            name='name',
            field=models.CharField(max_length=123, verbose_name='\u5546\u54c1\u540d'),
        ),
        migrations.AlterField(
            model_name='smalltype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 30, 13, 23, 49, 33719, tzinfo=utc)),
        ),
    ]
