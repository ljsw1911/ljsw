import secrets

from django.core.cache import cache
from django.http import JsonResponse

# 从数据库倒入数据表
from live_market.models import Goods


# 生活-商品的首页
def index(request):
    # token = request.GET.get('token')
    # current_user_id = cache.get(token)
    data = []
    goods_dict = {}
    goods = Goods.objects.all()
    for msg in goods:
        goods_dict['goods_id'] = msg.goods_id
        goods_dict['goods_name'] = msg.goods_name
        goods_dict['goods_pic'] = msg.goods_pic.split(',')[0]
        goods_dict['goods_price'] = msg.goods_price
        goods_dict['goods_sales'] = msg.goods_sales
        goods_dict['goods_category'] = msg.goods_category

        data.append(goods_dict)
        goods_dict = {}

    return JsonResponse({
        'code': 200,
        'msg': '商品信息展示',
        'data': data
    })


def details(request):
    data = {}
    goods_para = {}
    goods_id = request.GET.get('goods_id')
    goods = Goods.objects.filter(goods_id=goods_id).first()
    data['goods_name'] = goods.goods_name
    data['goods_pic'] = goods.goods_pic.split(',')
    data['goods_introduce'] = goods.goods_introduce
    data['goods_fright'] = goods.goods_freight
    data['goods_price'] = goods.goods_price
    data['goods_sales'] = goods.goods_sales

    goods_para['address'] = goods.address
    goods_para['packaging'] = goods.packaging
    goods_para['specifications'] = goods.specifications
    data['goods_para'] = goods_para

    return JsonResponse({
        'code':200,
        'msg':'商品详情',
        'data':data,
    })