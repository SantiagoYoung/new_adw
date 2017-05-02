# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_auto_20161201_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselFigure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=123, verbose_name='\u56fe\u7247\u540d\u79f0')),
                ('picture', models.ImageField(upload_to=b'carousel/', verbose_name='\u8f6e\u64ad\u56fe')),
                ('create_time', models.DateTimeField(verbose_name=datetime.datetime(2016, 12, 1, 8, 28, 22, 949641, tzinfo=utc))),
                ('edit_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u8f6e\u64ad\u56fe',
                'verbose_name_plural': '\u8f6e\u64ad\u56fe',
            },
        ),
        migrations.RenameField(
            model_name='goods',
            old_name='price',
            new_name='origin_price',
        ),
        migrations.AddField(
            model_name='goods',
            name='new_price',
            field=models.FloatField(default=None, max_length=123, verbose_name='\u73b0\u4ef7'),
        ),
        migrations.AlterField(
            model_name='bigtype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 1, 8, 28, 22, 950335, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='goods',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 1, 8, 28, 22, 951902, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='smalltype',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 1, 8, 28, 22, 951071, tzinfo=utc)),
        ),
    ]
