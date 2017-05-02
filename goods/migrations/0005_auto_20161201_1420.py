# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_auto_20161201_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='bigtype',
            name='picture1',
            field=models.ImageField(default=None, upload_to=b'big_type/', verbose_name='\u5927\u7c7b\u56fe\u72471'),
        ),
        migrations.AddField(
            model_name='bigtype',
            name='picture2',
            field=models.ImageField(default=None, upload_to=b'big_type/', verbose_name='\u5927\u7c7b\u56fe\u72472'),
        ),
        migrations.AlterField(
            model_name='bigtype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 1, 6, 20, 34, 434069, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='goods',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 1, 6, 20, 34, 435456, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='smalltype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 1, 6, 20, 34, 434821, tzinfo=utc)),
        ),
    ]
