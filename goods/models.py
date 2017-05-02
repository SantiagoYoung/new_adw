# coding: utf-8
from django.db import models
from django.utils import timezone
from account.models import User




class CarouselFigure(models.Model):

    name = models.CharField(max_length=123, verbose_name=u'图片名称')
    picture = models.ImageField(upload_to='carousel/', verbose_name=u'轮播图')

    create_time = models.DateTimeField(default=timezone.now())
    edit_time = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class BigType(models.Model):
    name = models.CharField(max_length=123, verbose_name=u'大类')
    english_name = models.CharField(max_length=123, verbose_name=u'英语名', default=None)

    create_time = models.DateTimeField(default=timezone.now())

    picture1 = models.ImageField(upload_to='big_type/', verbose_name=u'大类图片1', default=None)
    picture2 = models.ImageField(upload_to='big_type/', verbose_name=u'大类图片2', default=None)

    class Meta:
        verbose_name = u'大类'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name

class SmallType(models.Model):

    big_type = models.ForeignKey(BigType, related_name='small')

    name = models.CharField(max_length=123, verbose_name=u'小类')

    create_time = models.DateTimeField(default=timezone.now())

    class Meta:
        verbose_name = u'小类'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Goods(models.Model):


    SHOW_TYPE = (
        (0, u'不展示'),
        (1, u'展示'),
    )
    GOODS_STATUS =(
        (0, u'审核未通过'),
        (1, u'审核中'),
        (2, u'审核通过'),
    )

    small_type = models.ForeignKey(SmallType, related_name='goods')
    seller = models.ForeignKey(User, verbose_name=u'卖家', blank=True, null=True, related_name='goods_seller')

    collecters = models.ManyToManyField(User, verbose_name=u'收藏者', null=True, blank=True)

    store = models.ForeignKey('store.Store', verbose_name=u'店铺', null=True, blank=True)

    # collector = models.ManyToManyField(User, verbose_name=u'收藏者', null=True, blank=True, related_name='goods_collector')

    # is_collected = models.BooleanField(default=False, verbose_name=u'是否被收藏')
    collected_number = models.IntegerField(default=12, null=True, blank=True, verbose_name=u'收藏数')
    goods_stock = models.IntegerField(default=12, null=True, blank=True, verbose_name=u'库存')

    goods_status = models.IntegerField(max_length=1, verbose_name=u'商品审核状态', default=0, choices=GOODS_STATUS)
    show_type = models.IntegerField(max_length=1, verbose_name=u'商品展示类型', default=0, choices=SHOW_TYPE)

    provide_design = models.BooleanField(verbose_name=u'提供设计', default=False)
    provide_produce = models.BooleanField(verbose_name=u'提供制作', default=False)

    custom_size = models.BooleanField(verbose_name=u'定制尺寸', default=False)
    custom_pattern = models.BooleanField(verbose_name=u'定制图案', default=False)
    custom_style = models.BooleanField(verbose_name=u'定制款式', default=False)


    name = models.CharField(max_length=123, verbose_name=u'商品名')
    description = models.CharField(max_length=213, verbose_name=u'商品描述', default=None)
    origin_price = models.FloatField(max_length=123, verbose_name=u'价格', default=None)
    new_price = models.FloatField(max_length=123, verbose_name=u'现价', default=None)
    colors = models.CharField(max_length=123, verbose_name=u'商品颜色', default=u'无')

    picture = models.ImageField(upload_to='goods/',verbose_name=u'图片', default=None)

    create_time = models.DateTimeField(default=timezone.now(), verbose_name=u'发布时间')


    class Meta:
        verbose_name = u'商品'
        verbose_name_plural = verbose_name


    def __unicode__(self):
        return self.name


class GoodsCollection(models.Model):

    user = models.ManyToManyField(User, verbose_name=u'收藏者')
    goods = models.OneToOneField(Goods)
    # is_collected = models.BooleanField(default=False, verbose_name=u'是否被收藏')
    # collected_number = models.IntegerField(default=0, verbose_name=u'被收藏数')
    collected_time = models.DateTimeField(default=timezone.now())


    class Meta:
        verbose_name = u'商品收藏'
        verbose_name_plural= verbose_name

    def __unicode__(self):
        return self.goods.name





