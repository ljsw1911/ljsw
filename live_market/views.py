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
        goods_dict['goods_pic'] = msg.goods_pic.split(',')
        goods_dict['goods_introduce'] = msg.goods_introduce
        goods_dict['goods_fright'] = msg.goods_freight
        goods_dict['goods_price'] = msg.goods_price
        goods_dict['goods_num'] = msg.goods_num
        goods_dict['goods_sales'] = msg.goods_sales
        goods_dict['goods_category'] = msg.goods_category
        goods_dict['goods_para'] = msg.goods_para.split(',')

        data.append(goods_dict)
        goods_dict = {}

    return JsonResponse({
        'code': 200,
        'msg': '商品信息展示',
        'goods_list': data
    })