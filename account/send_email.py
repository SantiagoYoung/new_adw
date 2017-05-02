# coding=utf-8

from django.core.mail import EmailMultiAlternatives

class SendEmail(object):
    def __init__(self, subject, sender, receiver, text, html):
        self.subject = subject
        self.sender = sender
        self.reveiver = receiver
        self.text = text
        self.html = html

    def send(self):
        msg = EmailMultiAlternatives(self.subject, self.text,
                                     self.sender, [self.reveiver,],
                                     )
        msg.attach_alternative(self.html, 'text/html')
        msg.send()

import time
import threading
from Queue import Queue
from random import random
from views import send_mail
'''
接受请求

将 发送 邮件的函数加入队列中。
然后使用threading 进行同步执行
'''





































































