# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BigType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=123, verbose_name='\u5927\u7c7b')),
                ('create_time', models.DateTimeField(verbose_name=datetime.datetime(2016, 11, 30, 8, 9, 31, 795445, tzinfo=utc))),
            ],
            options={
                'verbose_name': '\u5927\u7c7b',
                'verbose_name_plural': '\u5927\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=123)),
            ],
        ),
        migrations.CreateModel(
            name='SmallType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=123, verbose_name='\u5c0f\u7c7b')),
                ('create_time', models.DateTimeField(verbose_name=datetime.datetime(2016, 11, 30, 8, 9, 31, 795931, tzinfo=utc))),
                ('big_type', models.ForeignKey(to='goods.BigType')),
            ],
            options={
                'verbose_name': '\u5c0f\u7c7b',
                'verbose_name_plural': '\u5c0f\u7c7b',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='small_type',
            field=models.ForeignKey(to='goods.SmallType'),
        ),
    ]
