# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_collected', models.BooleanField(default=False, verbose_name='\u662f\u5426\u88ab\u6536\u85cf')),
                ('company_form', models.CharField(default=0, max_length=1, choices=[(0, '\u516c\u53f8'), (1, '\u4e2a\u4eba')])),
                ('store_status', models.CharField(default=3, max_length=1, choices=[(1, '\u5ba1\u6838\u4e2d'), (2, '\u5ba1\u6838\u901a\u8fc7'), (3, '\u5ba1\u6838\u672a\u901a\u8fc7')])),
                ('store_style', models.CharField(default=0, max_length=1, choices=[(0, '\u5236\u4f5c(\u63d0\u4f9b\u6750\u6599)'), (1, '\u8bbe\u8ba1'), (2, '\u79c1\u4eba\u8ba2\u5236'), (3, '\u5de5\u88c5\u5b9a\u5236')])),
                ('store_name', models.CharField(max_length=123, verbose_name='\u5e97\u540d')),
                ('phone', models.CharField(max_length=123, verbose_name='\u7535\u8bdd')),
                ('qq', models.CharField(max_length=123, verbose_name='qq')),
                ('introduction', models.TextField(verbose_name='\u5e97\u94fa\u4ecb\u7ecd')),
                ('head_picture', models.ImageField(upload_to=b'store/', verbose_name='\u516c\u53f8LoGo')),
                ('company_name', models.CharField(max_length=123, verbose_name='\u516c\u53f8\u540d')),
                ('corporation', models.CharField(max_length=123, verbose_name='\u516c\u53f8\u6cd5\u4eba')),
                ('phone_number', models.CharField(max_length=123, verbose_name='\u516c\u53f8\u7535\u8bdd')),
                ('address', models.CharField(max_length=123, verbose_name='\u516c\u53f8\u5730\u5740')),
                ('company_qq', models.CharField(max_length=123, verbose_name='\u516c\u53f8QQ')),
                ('license', models.ImageField(upload_to=b'license/', verbose_name='\u516c\u53f8\u8425\u4e1a\u6267\u7167')),
                ('company_introduction', models.TextField(max_length=123, verbose_name='\u516c\u53f8\u7b80\u4ecb')),
                ('collector', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, verbose_name='\u6536\u85cf\u7684\u4eba', blank=True)),
                ('owner', models.OneToOneField(related_name='boss', null=True, blank=True, to=settings.AUTH_USER_MODEL, verbose_name='\u8001\u677f')),
            ],
            options={
                'verbose_name': '\u5e97\u94fa',
                'verbose_name_plural': '\u5e97\u94fa',
            },
        ),
    ]
