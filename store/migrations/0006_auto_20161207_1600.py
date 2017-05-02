# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20161207_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sotrecollection',
            name='collected_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 8, 0, 25, 554366, tzinfo=utc)),
        ),
    ]
