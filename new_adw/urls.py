# coding: utf-8

"""new_adw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from account import views
urlpatterns = [


    url(r'^admin/', include(admin.site.urls)),

    url(r'^account/', include('account.urls')),
    url(r'^goods/', include('goods.urls')),
    url(r'^store/', include('store.urls')),
    url(r'^message/', include('message.urls')),

    url(r'^$', views.home),                 #首页
    url(r'login', views.login_page),        #登录
    url(r'register', views.register_page),  #注册
    url(r'question', views.question_page),  #问问
    url(r'apply', views.apply_page),        #店铺入驻
    url(r'center', views.center_page),      #个人中心




]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)