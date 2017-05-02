from django.shortcuts import render

from goods.models import Goods
from store.models import Store
from check.custom_response import Json_Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.core.paginator import Page, PageNotAnInteger, EmptyPage, InvalidPage, Paginator


@csrf_exempt
def search(request):

    if request.method == 'POST':

        goods = request.POST.get('goods', None)
        store = request.POST.get('store', None)
        page  = request.POST.get('page', None)

        if goods:
            results = Goods.objects.filter(Q(name__icontains=goods) | Q(description__icontains=goods))

            paginator = Paginator(results, 1)
            try:
                goods_results = paginator.page(page)
            except (PageNotAnInteger,InvalidPage):
                goods_results = paginator.page(1)
            except EmptyPage:
                goods_results = paginator.page(paginator.num_pages)

            l = []
            for goods_result in goods_results:
                d = dict()
                d['id'] = goods_result.id
                d['name'] = goods_result.name
                l.append(d)

            return Json_Response(l)
        if store:
            results = Store.objects.filter(Q(store_name__icontains=store) | Q(introduction__icontains=store))

            paginator = Paginator(results, 1)
            try:
                store_results = paginator.page(page)
            except (PageNotAnInteger,InvalidPage):
                store_results = paginator.page(1)
            except EmptyPage:
                store_results = paginator.page(paginator.num_pages)

            l = []
            for store_result in store_results:
                d = dict()
                d['id'] = store_result.id
                d['store_name'] = store.store_name
                d['boss'] = store.owner.username
                l.append(d)
            return Json_Response(l)

    return JsonResponse({'status': 0 })






























