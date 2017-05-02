# coding: utf-8

from django.shortcuts import render

from models import BigType, SmallType, Goods, GoodsCollection
from serializers import BigTypeSerializer, SmallTypeSerializer, GoodsSerializer
from rest_framework import viewsets

from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from check.custom_response import Json_Response
from account.models import User
from store.models import Store

from django.core.cache import cache



class BigTypeViewSet(viewsets.ModelViewSet):

    queryset = BigType.objects.all()
    serializer_class = BigTypeSerializer


# class SmallTypeViewSet(viewsets.ModelViewSet):
#
#     queryset = SmallType.objects.all()
#     serializer_class = SmallTypeSerializer


# def big_types(request):
#
#     big_types = BigType.objects.all()
#     l = []
#     for big_type in big_types:
#         d = dict()
#         d['id'] = big_type.id
#         d['name'] = big_type.name
#         l.append(d)
#     return Json_Response(l)

@csrf_exempt
def get_small_types(request):

    if request.method == 'POST':

        id = request.POST.get('id', None)
        print id

        try:
            big_type = BigType.objects.get(pk=id)
        except BigType.DoesNotExist:
            return JsonResponse({'status': 0, 'message': 'no such big type'})

        small_types = SmallType.objects.select_related().filter(big_type=big_type)


        l = []
        for small_type in small_types:
            d = dict()
            d['id'] = small_type.id
            d['name'] = small_type.name
            l.append(d)

        return Json_Response(l)
    return JsonResponse({'status': 0})


@csrf_exempt
def get_small_type_goods(request):

    if request.method == 'POST':
        id = request.POST.get('id', None)

        try:
            small_type = SmallType.objects.get(pk=id)
        except SmallType.DoesNotExist:
            return JsonResponse({'status': 0, 'message':'no such small type'})

        goods = Goods.objects.select_related().filter(small_type=small_type)

        l = []
        for good in goods:
            d = dict()
            d['id'] = good.id
            d['name'] = good.name
            d['origin_price'] = good.origin_price
            d['description'] = good.description
            d['picture'] = good.picture.url
            l.append(d)

        return Json_Response(l)
    return JsonResponse({'status': 0})



# 首页大类展示，后面展示6张图片
@csrf_exempt
def show_picture(request):

    big_types = BigType.objects.select_related().all()

    l = []

    for big_type in big_types:

        small_types = SmallType.objects.select_related().filter(big_type=big_type)
        d = dict()
        d['big_group'] = dict()
        d['big_group']['big_name'] = big_type.name
        d['big_group']['big_english_name'] = big_type.english_name
        d['big_group']['picture1'] = big_type.picture1.url
        d['big_group']['picture2'] = big_type.picture2.url
        d['big_group']['small_group'] = list()
        for small_type in small_types:

            goods = Goods.objects.select_related().filter(small_type=small_type)[0:8] #拿6张照片
            # d[big_type.name][small_type.name] = dict()
            small_type.name = dict()
            for good in goods:

                # d[big_type.name][small_type.name]['id'] = good.id
                # d[big_type.name][small_type.name]['picture'] = good.picture.url
                # d[big_type.name][small_type.name]['description'] = good.description
                # d[big_type.name][small_type.name]['origin_price'] = good.origin_price
                small_type.name['id'] = good.id
                small_type.name['picture'] = good.picture.url
                small_type.name['description'] = good.description
                small_type.name['origin_price'] = good.origin_price

            d['big_group']['small_group'].append(small_type.name)
        l.append(d)

    return Json_Response(l)

@csrf_exempt
def goods_detail(request):

    if request.method == 'POST':
        id = request.POST.get('id', None)
        try:
            goods = Goods.objects.get(pk=id)
            print goods
        except Goods.DoesNotExist:
            return Json_Response({'status': 0, 'message': 'no such goods'})

        try:
            store = Store.objects.get(goods=goods)
        except Store.DoesNotExist:
            return JsonResponse({'status': 0})

        l = []
        d = dict()
        d['name'] = goods.name
        d['id'] = goods.id
        d['origin_price'] = goods.origin_price
        d['new_price'] = goods.new_price
        d['picture'] = goods.picture.url
        d['store_name'] = store.store_name
        l.append(d)
        print '2dddddddddddddddddd'
        return Json_Response(l)
    return JsonResponse({'status': 0})



class EditGoodsViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UploadGoods(APIView):

    def get(self, request, format=None):

        user = request.user
        print user

        l = []
        d = dict()
        for big_type in BigType.objects.all():
            # d[big_type.name] = dict()
            d[big_type.name] = list()
            for small_type in SmallType.objects.filter(big_type=big_type):
                # d[big_type.name][small_type.name] = small_type.name
                d[big_type.name].append(small_type.name)
        l.append(d)

        return Response(l)


    def post(self, request, format=None):

        # user = request.user
        user = User.objects.get(username=123)
        print user, '********'

        small_type = request.data.get('small_type', None)
        collected_number = request.data.get('collected_number', None)
        goods_stock = request.data.get('goods_stock', None)
        provide_design = request.data.get('provide_design', None)
        provide_produce = request.data.get('provide_produce', None)
        custom_size = request.data.get('custom_size', None)
        custom_pattern = request.data.get('custom_pattern', None)
        custom_style = request.data.get('custom_style', None)
        name = request.data.get('name', None)
        description = request.data.get('description', None)
        origin_price = request.data.get('origin_price', None)
        new_price = request.data.get('new_price', None)
        colors = request.data.get('colors', None)
        picture = request.data.get('picture', None)
        try:
            Goods.objects.create(small_type=small_type, seller=user, collected_number=collected_number,
                                 goods_stock=goods_stock, provide_design=provide_design, provide_produce=provide_produce,
                                 custom_size=custom_size, custom_pattern=custom_pattern, custom_style=-custom_style,
                                 name=name, description=description, origin_price=origin_price, new_price=new_price,
                                 colors=colors, picture=picture,
            )
        except:
            return JsonResponse({ 'status': -1 })

        return Response({'statas': 0})



@csrf_exempt
def collect_goods(request):

    # user = request.user
    user = User.objects.get(username=123)

    # print cache.get('user'), '$$$$$$$$$$$$$$$$$$$$$$$$$$$'

    if not user:
        return JsonResponse({'status': 0})

    if request.method == 'POST':

        status = int(request.POST.get('status', None))

        id = request.POST.get('id', None)
        try:
            goods = Goods.objects.get(pk=id)
        except Goods.DoesNotExist:
            return JsonResponse({'status': -9})

        try:
            collection = GoodsCollection.objects.get(goods=goods)
        except GoodsCollection.DoesNotExist:
            collection = GoodsCollection.objects.create(goods=goods)
        if status == 1:
            collection.user.add(user)
            return JsonResponse({'status': 1, 'message': 'success'})
        if status == 0:
            collection.user.remove(user)
            return JsonResponse({'status': 0, 'message': 'cancle'})
    return JsonResponse({'status': 0})



@csrf_exempt
def collect(request):

    # user = request.user
    user = User.objects.get(username=123)

    # cache.set('user', user, 60 * 2)

    if request.method == 'POST':
        id = request.POST.get('id', None)
        status = request.POST.get('status', None)
        status = int(status)
        try:
            goods = Goods.objects.get(pk=id)
        except Goods.DoesNotExist:
            return JsonResponse({'status': 2, 'message': 'not exist'})
        if status == 1:
            goods.collecters.add(user)
            goods.save()
            return JsonResponse({'status': 1, 'message': 'success'})
        elif status == 0:
            goods.collecters.remove(user)
            goods.save()
            return JsonResponse({'status': 3, 'message': 'cancle'})
    return JsonResponse({'status': 0 })































