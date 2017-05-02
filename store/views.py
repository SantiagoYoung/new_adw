from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from models import Store, SotreCollection
from django.http import JsonResponse
from account.models import User
from check.custom_response import Json_Response
from goods.models import Goods, GoodsCollection

@csrf_exempt
def store_apply(request):

    if request.method == 'POST':
        # store
        # owner = request.user
        owner = User.objects.get(username=123)

        store_name = request.POST.get('store_name', None)
        phone = request.POST.get('phone', None)
        qq = request.POST.get('qq', None)
        introduction = request.POST.get('introduction', None)
        company_form = int(request.POST.get('company_form', None))
        # store_status = request.POST.get('store_status', None)
        store_style =int(request.POST.get('store_style', None))
        print store_style,'>>>.'
        print company_form, '>>>'
        # company
        head_picture = request.POST.get('head_picture', None)
        company_name = request.POST.get('company_name', None)
        corporation = request.POST.get('corporation', None)
        phone_number = request.POST.get('phone_number', None)
        address = request.POST.get('address', None)
        company_qq = request.POST.get('company_qq', None)
        license = request.POST.get('license', None)
        company_introduction = request.POST.get('company_introduction', None)


        if Store.objects.filter(owner=owner):
            return JsonResponse({'status': 0})

        try:
            Store.objects.create(
                owner=owner, store_name=store_name, phone=phone, qq=qq,
                introduction=introduction, company_form=company_form,
                store_style=store_style,
                head_picture=head_picture, company_name=company_name, corporation=corporation,
                phone_number=phone_number, address=address, company_qq=company_qq,
                license = license, company_introduction=company_introduction
            )
        except:
            return JsonResponse({'status': 0, 'message': ' problem '})
    return JsonResponse({'status': 0})


def store_edit(request):

    owner = request.user

    store = Store.objects.select_related().filter(owner=owner)

    if request.method == 'GET':

        l = []
        d = dict()
        d['store_name '] = store.store_name
        d['phone'] = store.phone
        d['qq'] = store.qq
        d['introduction'] = store.introduction
        d['company_form'] = store.company_form
        d['store_style'] = store.store_style
        d['head_picture'] = store.head_picture
        d['company_name'] = store.company_name
        d['corporation'] = store.corporation
        d['phone_number'] = store.phone_number
        d['address'] = store.address
        d['company_qq'] = store.company_qq
        d['license'] = store.license
        d['company_introduction'] = store.company_introduction
        l.append(d)
        return Json_Response(l)

    if request.method == 'POST':

        # owner = request.user
        # owner = User.objects.filter(username=123)
        store_name = request.POST.get('store_name', None)
        phone = request.POST.get('phone', None)
        qq = request.POST.get('qq', None)
        introduction = request.POST.get('introduction', None)
        company_form = int(request.POST.get('company_form', None))
        store_style =int(request.POST.get('store_style', None))
        head_picture = request.POST.get('head_picture', None)
        company_name = request.POST.get('company_name', None)
        corporation = request.POST.get('corporation', None)
        phone_number = request.POST.get('phone_number', None)
        address = request.POST.get('address', None)
        company_qq = request.POST.get('company_qq', None)
        license = request.POST.get('license', None)
        company_introduction = request.POST.get('company_introduction', None)

        try:
            store(store_name=store_name, phone=phone, qq=qq, introduction=introduction,
                  company_form=company_form, store_style=store_style, head_picture=head_picture,
                  company_name=company_name, corporation=corporation, phone_number=phone_number,
                  address=address, company_qq=company_qq, license=license, company_introduction=company_introduction)
        except:
            return JsonResponse({'status': 0})

        store.save()

        return JsonResponse({'status': 1 , 'message': 'success'})
    return JsonResponse({'status': 0})





def upload_goods(request):

    pass


@csrf_exempt
def collect_store(request):

    # user = request.user
    user = User.objects.get(username=123)

    if request.method == 'POST':

        status = int(request.POST.get('status', None))
        id = request.POST.get('id', None)


        goods = Goods.objects.get(pk=id)
        store = Store.objects.get(goods=goods)

        try:
            collections = SotreCollection.objects.get(store=store)
        except SotreCollection.DoesNotExist:
            collections = SotreCollection.objects.create(store=store)

        if status == 1:
            collections.user.add(user)
            # collections.user.add(User.objects.get(username='admin'))
            return JsonResponse({'status': 1, 'message': 'sucess'})

        if status == 0:
            collections.user.remove(user)
            return JsonResponse({'status': 0, 'message': 'cancle'})

    return JsonResponse({'status': 0})


@csrf_exempt
def collect(request):

    # user = request.user
    user = User.objects.get(username=123)

    if request.method == 'POST':
        id = request.POST.get('id', None)
        status = request.POST.get('status', None)
        status = int(status)
        try:
            goods = Goods.objects.get(pk=id)
        except Goods.DoesNotExist:
            return JsonResponse({'status': -1, 'message': 'no no no '})
        store = Store.objects.get(goods=goods)
        if status == 1:
            store.collecter.add(user)
            return JsonResponse({'status': 1, 'message': 'success'})
        elif status == 0:
            store.collector.remove(user)
            return JsonResponse({'status': -1, 'message': 'cancle'})

    return JsonResponse({'status': 0 })














































