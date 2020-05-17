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
from django.urls import path, include

from ordermsg import views

app_name = 'ordermsg'
urlpatterns = {
    path('order/msg/', views.ordermsg, name='ordermsg'),
    path('order/info/', views.orderinfo, name='orderinfo'),
    path('order/complete/', views.complete, name='complete'),
    path('order/delete/', views.delete, name='delete'),


}
