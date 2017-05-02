# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0007_auto_20161202_1028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='collector',
        ),
        migrations.AlterField(
            model_name='bigtype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 2, 3, 26, 43, 941886, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='carouselfigure',
            name='create_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 12, 2, 3, 26, 43, 941119, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='goods',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 2, 3, 26, 43, 943804, tzinfo=utc), verbose_name='\u53d1\u5e03\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='smalltype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 2, 3, 26, 43, 942695, tzinfo=utc)),
        ),
    ]
