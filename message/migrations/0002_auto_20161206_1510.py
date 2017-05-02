# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggesstion',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 6, 7, 10, 19, 765796, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='systeminformation',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 6, 7, 10, 19, 765287, tzinfo=utc)),
        ),
    ]
