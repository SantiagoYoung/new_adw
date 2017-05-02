# coding: utf-8
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager


class MyBaseUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('The given username must be set')

        user = self.model(username=username)
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password)

        user.is_admin = True

        user.save(using=self._db)

        return user



class User(AbstractBaseUser):

    username = models.CharField(verbose_name=u'用户名',max_length=40, unique=True)

    join_time = models.DateTimeField(default=timezone.now())

    is_active = models.BooleanField(default=True, verbose_name=u'激活')
    is_staff = models.BooleanField(default=False, verbose_name=u'管理员')
    is_admin = models.BooleanField(default=False, verbose_name=u'超级管理员')

    objects = MyBaseUserManager()
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = verbose_name


    def __unicode__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin


class Vip(models.Model):

    user = models.OneToOneField(User)

    qq = models.CharField(max_length=13, verbose_name=u'QQ', null=True, blank=True)
    nickname = models.CharField(max_length=99, verbose_name=u'昵称', default='uu', null=True, blank=True)
    phone = models.CharField(max_length=19, verbose_name=u'电话号码', null=True, blank=True)



    class Meta:
        verbose_name = u'会员'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.user.username




























class MessageType(models.Model):

    title = models.CharField(max_length=99, verbose_name=u'留言类型', default=u'定制问问')
    create_time = models.DateTimeField(default=timezone.now())

    class Meta:
        verbose_name = u'留言类型'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.title


class MessageBoard(models.Model):

    username = models.CharField(max_length=999, verbose_name=u'用户名', null=True, blank=True)

    content = models.TextField(verbose_name=u'留言信息')
    contact = models.CharField(max_length=999, verbose_name=u'联系方式')

    creat_time = models.DateTimeField(default=timezone.now())

    class Meta:
        verbose_name = u'留言板'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.content


class Reply(models.Model):

    username = models.CharField(default=u'卖家大人', max_length=123)
    message = models.OneToOneField(MessageBoard)

    reply_time = models.DateTimeField(default=timezone.now())
    content = models.TextField()

    class Meta:
        verbose_name = u'回复'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.content




































