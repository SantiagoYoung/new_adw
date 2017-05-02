# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('username', models.CharField(unique=True, max_length=40, verbose_name='\u7528\u6237\u540d')),
                ('join_time', models.DateTimeField(default=datetime.datetime(2016, 11, 30, 8, 2, 21, 809371, tzinfo=utc))),
                ('is_active', models.BooleanField(default=True, verbose_name='\u6fc0\u6d3b')),
                ('is_admin', models.BooleanField(default=False, verbose_name='\u8d85\u7ea7\u7ba1\u7406\u5458')),
            ],
            options={
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
        migrations.CreateModel(
            name='MessageBoard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=999, null=True, verbose_name='\u7528\u6237\u540d', blank=True)),
                ('content', models.TextField(verbose_name='\u7559\u8a00\u4fe1\u606f')),
                ('contact', models.CharField(max_length=999, verbose_name='\u8054\u7cfb\u65b9\u5f0f')),
                ('creat_time', models.DateTimeField(default=datetime.datetime(2016, 11, 30, 8, 2, 21, 811420, tzinfo=utc))),
            ],
            options={
                'verbose_name': '\u7559\u8a00\u677f',
                'verbose_name_plural': '\u7559\u8a00\u677f',
            },
        ),
        migrations.CreateModel(
            name='MessageType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default='\u5b9a\u5236\u95ee\u95ee', max_length=99, verbose_name='\u7559\u8a00\u7c7b\u578b')),
                ('create_time', models.DateTimeField(default=datetime.datetime(2016, 11, 30, 8, 2, 21, 810779, tzinfo=utc))),
            ],
            options={
                'verbose_name': '\u7559\u8a00\u7c7b\u578b',
                'verbose_name_plural': '\u7559\u8a00\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(default='\u5356\u5bb6\u5927\u4eba', max_length=123)),
                ('reply_time', models.DateTimeField(default=datetime.datetime(2016, 11, 30, 8, 2, 21, 811975, tzinfo=utc))),
                ('content', models.TextField()),
                ('message', models.OneToOneField(to='account.MessageBoard')),
            ],
            options={
                'verbose_name': '\u56de\u590d',
                'verbose_name_plural': '\u56de\u590d',
            },
        ),
        migrations.CreateModel(
            name='Vip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qq', models.CharField(max_length=13, null=True, verbose_name='QQ', blank=True)),
                ('nickname', models.CharField(default=b'uu', max_length=99, null=True, verbose_name='\u6635\u79f0', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u4f1a\u5458',
                'verbose_name_plural': '\u4f1a\u5458',
            },
        ),
    ]
