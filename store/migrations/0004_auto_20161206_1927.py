# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20161206_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sotrecollection',
            name='collected_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 6, 11, 27, 31, 719035, tzinfo=utc)),
        ),
    ]
