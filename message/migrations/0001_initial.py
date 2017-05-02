# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suggesstion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name='\u5efa\u8bae\u5185\u5bb9')),
                ('create_time', models.DateTimeField(default=datetime.datetime(2016, 12, 6, 6, 59, 8, 161263, tzinfo=utc))),
            ],
            options={
                'verbose_name': '\u6295\u8bc9\u5efa\u8bae',
                'verbose_name_plural': '\u6295\u8bc9\u5efa\u8bae',
            },
        ),
        migrations.CreateModel(
            name='SystemInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=123, verbose_name='\u6807\u9898')),
                ('message', models.TextField(verbose_name='\u7cfb\u7edf\u6d88\u606f')),
                ('username', models.CharField(default='\u6765\u81ea\u7cfb\u7edf', max_length=123)),
                ('created_time', models.DateTimeField(default=datetime.datetime(2016, 12, 6, 6, 59, 8, 160639, tzinfo=utc))),
            ],
            options={
                'verbose_name': '\u7cfb\u7edf',
                'verbose_name_plural': '\u7cfb\u7edf',
            },
        ),
    ]
