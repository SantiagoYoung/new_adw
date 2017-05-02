# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20161207_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='is_collected',
        ),
        migrations.AlterField(
            model_name='sotrecollection',
            name='collected_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 7, 8, 22, 30, 136436, tzinfo=utc)),
        ),
    ]
