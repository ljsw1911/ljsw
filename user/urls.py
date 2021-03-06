"""ljsw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from user import views

app_name = 'user'
urlpatterns = [
    # 用户信息
    path('login/', views.user_login, name='user_login'),
    path('inspect/', views.user_inspect, name='user_inspect'),
    path('code/', views.get_code, name='get_code'),
    path('userinfo/', views.userinfo, name='userinfo'),
    path('getmsg/', views.get_msg, name='modify'),
    path('modify/', views.modify, name='modify'),
    # 地址
    path('addres/', views.addres, name='addres'),
    path('modadr/single/', views.mod_addres_single, name='modadrsingle'),
    path('modadr/', views.mod_addres, name='mod_addres'),
    path('deladr/', views.del_addres, name='del_addres'),
    # 积分
    path('points/', views.points, name='points'),
    path('pointform/', views.points_form, name='points_form'),
    path('exchange/', views.exchange, name='exchange'),
    # 上门回收订单显示
    path('recycle/order/', views.recycle_order, name='recycle_order'),
    # path('recycle/choice/', views.recycle_order_choice, name='recycle_order_choice'),
    path('rec/com_cle/', views.rec_com_cle, name='rec_com_cle'),
    # 商城订单显示


]
