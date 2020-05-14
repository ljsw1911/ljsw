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
    #用户信息
    path('login/', views.user_login, name='user_login'),
    path('inspect/', views.user_inspect, name='user_inspect'),
    path('code/', views.get_code, name='get_code'),
    path('userinfo/', views.userinfo, name='userinfo'),
    path('getmsg/', views.get_msg, name='modify'),
    path('modify/', views.modify, name='modify'),
    #地址
    path('addres/', views.addres, name='addres'),
    path('modadrsingle/', views.mod_addres_single, name='addres'),
    path('modadr/', views.mod_addres, name='mod_addres'),
    path('deladr/', views.del_addres, name='del_addres'),
    #积分
    path('points/', views.del_addres, name='del_addres'),



]
