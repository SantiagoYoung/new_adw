# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0002_remove_store_collector'),
    ]

    operations = [
        migrations.CreateModel(
            name='SotreCollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('collected_time', models.DateTimeField(default=datetime.datetime(2016, 12, 6, 7, 10, 19, 763969, tzinfo=utc))),
            ],
            options={
                'verbose_name': '\u5e97\u94fa\u6536\u85cf',
                'verbose_name_plural': '\u5e97\u94fa\u6536\u85cf',
            },
        ),
        migrations.AddField(
            model_name='store',
            name='collected_number',
            field=models.IntegerField(default=0, verbose_name='\u88ab\u6536\u85cf\u6570'),
        ),
        migrations.AddField(
            model_name='sotrecollection',
            name='store',
            field=models.OneToOneField(to='store.Store'),
        ),
        migrations.AddField(
            model_name='sotrecollection',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='\u6536\u85cf\u8005'),
        ),
    ]
