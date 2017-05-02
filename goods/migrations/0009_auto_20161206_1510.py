# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0008_auto_20161202_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsCollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('collected_time', models.DateTimeField(default=datetime.datetime(2016, 12, 6, 7, 10, 19, 761061, tzinfo=utc))),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u6536\u85cf',
                'verbose_name_plural': '\u5546\u54c1\u6536\u85cf',
            },
        ),
        migrations.AlterField(
            model_name='bigtype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 6, 7, 10, 19, 758198, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='carouselfigure',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 6, 7, 10, 19, 757524, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='goods',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 6, 7, 10, 19, 759977, tzinfo=utc), verbose_name='\u53d1\u5e03\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='smalltype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 6, 7, 10, 19, 759056, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='goodscollection',
            name='goods',
            field=models.OneToOneField(to='goods.Goods'),
        ),
        migrations.AddField(
            model_name='goodscollection',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='\u6536\u85cf\u8005'),
        ),
    ]
