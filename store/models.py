# coding: utf-8
from django.db import models
from account.models import User
from django.utils import timezone

class Store(models.Model):


    COMPANY_FORM = (
        (0, u'公司'),
        (1, u'个人'),
    )
    STORE_STATUS = (
        (1, u'审核中'),
        (2, u'审核通过'),
        (3, u'审核未通过'),
    )
    STORE_STYLE = (
        (0,u'制作(提供材料)'),
        (1,u'设计'),
        (2,u'私人订制'),
        (3,u'工装定制'),
    )

    owner = models.OneToOneField(User, related_name='boss', verbose_name=u'老板', null=True, blank=True)

    collector = models.ManyToManyField(User, verbose_name=u'收藏者', null=True, blank=True)
    # seller_name = models.CharField(verbose_name=u'卖家名', null=True, blank=True)
    collected_number = models.IntegerField(default=0, verbose_name=u'被收藏数')

    company_form = models.IntegerField(max_length=2, default=0, choices=COMPANY_FORM)
    store_status = models.IntegerField(max_length=3, default=3, choices=STORE_STATUS)
    store_style = models.IntegerField(max_length=4, default=0, choices=STORE_STYLE)

    store_name = models.CharField(max_length=123, verbose_name=u'店名')
    phone = models.CharField(max_length=123, verbose_name=u'电话')
    qq = models.CharField(max_length=123, verbose_name=u'qq')
    introduction = models.TextField(verbose_name=u'店铺介绍')

    #公司信息
    head_picture = models.ImageField(upload_to='store/', verbose_name=u'公司LoGo')
    company_name = models.CharField(max_length=123, verbose_name=u'公司名',)
    corporation = models.CharField(max_length=123, verbose_name=u'公司法人')
    phone_number = models.CharField(max_length=123, verbose_name=u'公司电话')
    address = models.CharField(max_length=123, verbose_name=u'公司地址')
    company_qq = models.CharField(max_length=123, verbose_name=u'公司QQ')
    license = models.ImageField(upload_to='license/', verbose_name=u'公司营业执照')
    company_introduction = models.TextField(max_length=123, verbose_name=u'公司简介')

    class Meta:
        verbose_name = u'店铺'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.store_name


class SotreCollection(models.Model):

    user = models.ManyToManyField(User, verbose_name=u'收藏者', blank=True, null=True)
    store = models.OneToOneField(Store, blank=True, null=True)

    collected_time = models.DateTimeField(default=timezone.now())


    class Meta:
        verbose_name = u'店铺收藏'
        verbose_name_plural= verbose_name

    def __unicode__(self):
        return self.store.store_name















