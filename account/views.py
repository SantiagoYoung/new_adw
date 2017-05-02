# coding: utf-8
from django.shortcuts import render

from models import MessageBoard, Vip
from django.http import JsonResponse
from check.check import check_username
from check.custom_response import Json_Response

from serializers import MessageBoardSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from account.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from django.views.decorators.cache import cache_page

# @cache_page(60 * 15)
def home(request):
    return render(request, 'index.html')
def login_page(request):
    return render(request, 'login.html')
def register_page(request):
    return render(request, 'register.html')
def question_page(request):
    return render(request, 'question.html')
def apply_page(request):
    return render(request, 'store.html')
def center_page(request):
    return render(request, 'myidw.html')




@api_view(['GET', 'POST'])
def messages(request):

    if request.method == 'GET':
        messages = MessageBoard.objects.all()
        serializer = MessageBoardSerializer(messages, many=True)

        return Response(serializer.data)

    if request.method == 'POST':

        serializer = MessageBoardSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# register
# @api_view(['POST', 'GET'])
@csrf_exempt
def register(request):

    if request.method == 'POST':

        username = request.POST.get('username', None)
        qq = request.POST.get('qq')
        phone = request.POST.get('phone', None)
        nickname = request.POST.get('nickname', None)
        password = request.POST.get('password', None)
        confirm = request.POST.get('confirm', None)

        print username, qq, nickname, password, confirm


        if check_username(username):
            return JsonResponse({'status': 0, 'message': 'user has existed.'})

        if password != confirm:
            return JsonResponse({'status': 0, 'message': 'password not the same'})
        if check_username(username):
            return JsonResponse({'status': 0, 'message': 'user has existed.'})

        try:

            user = User.objects.create_user(username=username, password=password)

            print user

            Vip.objects.create(user=user, qq=qq, nickname=nickname, phone=phone)
        except Exception:
            return JsonResponse({'status': 0, 'message': 'no no no.'})

        return JsonResponse({'status': 1, 'message': 'success'})

    return JsonResponse({'status': 0 , 'message': 'see u again'})

# logout
def logout(request):
    auth.logout(request)
    return JsonResponse({'status': 1, 'message': 'logout successfully.'})


# login
@csrf_exempt
@api_view(['POST'])
def login(request):

    if request.method == 'POST':
        username = request.data.get('username')  # 邮箱
        password = request.data.get('password')

        try:
            User.objects.select_related().get(username=username)
        except User.DoesNotExist:
            return JsonResponse({'status': 0, 'message': 'no such user'})

        try:
            user = auth.authenticate(username=username, password=password)
            if not user:
                return JsonResponse({'status': 0, 'message': 'not valid user.'})

            auth.login(request, user)
            username = user.username

        except:
            return JsonResponse({'status': 0, 'message': 'try again'})

        return JsonResponse({"status": 1, 'message': 'success','username': username })

    return JsonResponse({'status': 0, 'message': 'not u'})




@csrf_exempt
@api_view(['POST','GET'])
# @login_required()
def change_password(request):

    user = request.user
    user = User.objects.get(username=111)

    if request.method == 'POST':
        old_password = request.POST.get("old_password")
        new_password = request.POST.get('new_password')
        confirm = request.POST.get('confirm')


        if old_password == None or new_password == None or confirm == None:
            return JsonResponse({'status': 0, 'message': 'empty'})

        if not user.check_password(old_password):
            return JsonResponse({'status': 0, 'message': 'not valid password'})

        if new_password != confirm:
            return JsonResponse({'status': 0, 'message': 'confirm password..'})

        user.set_password(new_password)
        user.save()

        return JsonResponse({'status': 1, 'message': 'success'})

    return JsonResponse({'status': 0})

from django.core.mail import send_mail
from check.check import get_code

@csrf_exempt
# @api_view(['POST'])
def forget_password(request):

    if request.method == 'POST':
        username = request.POST.get('username', None)
        verify_code = request.POST.get('verify_code',None)

        print username
        print verify_code

        if not username:
            return JsonResponse({'status': 0, 'message': 'empty'})
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({'status': 0, 'message': 'wrong email'})
        try:
            code = request.session.get(username).get('verify_code')
            print code,'>>>>>>>'
        except:
            return JsonResponse({'status': 0, 'message': 'code expire'})
        # code = get_code()
        # print code
        #
        # request.session['code'] = code
        # time = 60 * 10
        # request.session.set_expiry(time)
        #
        # text = u'你的验证码是 [%s]' % code
        #
        # send_mail(u'123', text,
        #           'santiago_young@163.com',
        #           [username], fail_silently=False)

        # if not request.session.get('code'):
        #     return JsonResponse({'status': 0, 'message': 'code expire'})

        if verify_code != code:
            return JsonResponse({'status': 0, 'message': 'code not the same'})

        request.session.set_expiry(0)

        return JsonResponse({'status': 1, 'message': 'success'})
    return JsonResponse({'status': 0})

@csrf_exempt
def get_verify_code(request):

    if request.method == 'POST':
        username = request.POST.get('username', None)

        if not username:
            return JsonResponse({'status': 0, 'message': 'empty'})
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({'status': 0, 'message': 'wrong email'})

        code = get_code()
        print code

        verify_code = {"verify_code": code}
        request.session[username] = verify_code
        time = 60 * 10
        request.session.set_expiry(time)

        text = u'你的验证码是 [%s]' % code
        subject = u'123'
        sender = 'santiago_young@163.com'

        # send_mail(subject, text,
        #           sender,
        #           [username],)
        from Queue import Queue
        q = Queue()
        q.put((send_mail, subject, text, sender, username))

        email = EmailThread(queue=q)

        import time
        time.sleep(5)

        return JsonResponse({'status':1, 'message': 'success'})
    return JsonResponse({'status': 0})

import threading
class EmailThread(threading.Thread):
    def __init__(self, queue):
        super(EmailThread, self).__init__()
        self._q = queue
        self.daemon = True
        self.start()
    def run(self):
        while 1:
            f, subject, text, sender, receiver = self._q.get()
            try:
                f(subject, text, sender, receiver)
            except Exception as e:
                print e
            self._q.task_done()






@csrf_exempt
@api_view(['POST'])
def reset_password(request):


    if request.method == 'POST':
        username = request.POST.get('username', None)
        new_password = request.POST.get('new_password', None)
        confirm = request.POST.get('confirm', None)

        print username, new_password, confirm

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({'status': 0, 'message': 'not valid user.'})

        if not new_password or not confirm:
            return JsonResponse({'status': 0, 'message': 'empty.'})

        if new_password != confirm:
            return JsonResponse({'status': 0, 'message': 'not the same password'})

        user.set_password(new_password)
        user.save()

        return JsonResponse({'status': 1, 'message': 'success'})

    return JsonResponse({"status": 0, 'message': 'nonono'})



@csrf_exempt
def user_information(request):

    if request.method == 'GET':
        # user = request.user
        user = User.objects.get(username=123)
        vip = Vip.objects.get(user=user)

        l = []
        d= dict()
        d['username'] = user.username
        d['phone'] = vip.phone
        d['qq'] = vip.qq
        d['nickname'] = vip.nickname
        l.append(d)
        return Json_Response(l)


    return JsonResponse({'status': 0})
























