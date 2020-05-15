import secrets

from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.utils import timezone

from django.db.models import Count

import datetime

# 从数据库倒入数据表
from live_market.models import ArticlePub, Collection, Praise, Focus, Comments,Goods


# 生活-商品的首页
def index(request):
    goods_list = []
    goods_dict = {}
    goods = Goods.objects.all()
    for msg in goods:
        goods_dict['goods_id'] = msg.goods_id
        goods_dict['goods_name'] = msg.goods_name
        goods_dict['goods_img'] = msg.goods_img
        goods_dict['goods_introduce'] = msg.goods_introduce
        goods_dict['goods_price'] = msg.goods_price
        goods_dict['goods_sales'] = msg.goods_sales

        goods_list.append(goods_dict)
        goods_dict = {}

    return JsonResponse({
        'code': 200,
        'msg': '商品信息展示',
        'goods_list': goods_list
    })