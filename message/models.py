# coding: utf-8
from django.db import models
from django.utils import timezone



class SystemInformation(models.Model):

    title = models.CharField(verbose_name=u'标题', max_length=123)
    message= models.TextField(verbose_name=u'系统消息')
    username = models.CharField(max_length=123, default=u'来自系统')
    created_time = models.DateTimeField(default=timezone.now())

    class Meta:
        verbose_name = u'系统'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title



class Suggesstion(models.Model):

    content = models.TextField(verbose_name=u'建议内容')

    create_time = models.DateTimeField(default=timezone.now())

    class Meta:
        verbose_name = u'投诉建议'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.content








