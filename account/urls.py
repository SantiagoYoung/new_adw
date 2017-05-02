
from django.conf.urls import url
import views

urlpatterns = [

    # message board.
    url(r'messages', views.messages, name='messages'),
    # url(r'message_board', views.message_board, name='message_board'),
    url(r'register', views.register, name='register'),
    url(r'login', views.login, name='login'),
    url(r'change_password', views.change_password, name='change_password'),

    url(r'forget_password', views.forget_password, name='forget_password'),
    url(r'reset_password', views.reset_password, name='reset_password'),
    url(r'get_verify_code', views.get_verify_code),
    url(r'user_information', views.user_information),

]




