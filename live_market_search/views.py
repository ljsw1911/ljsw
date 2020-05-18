from django.shortcuts import render
from django.http import JsonResponse

from live_market_search.models import Activity,Discount, Goods


# Create your views here.
def get_goods(request):
    # 获取商品名称  模糊查询
    goods = request.POST.get('goods')
    goods_data = Goods.objects.filter(goods_name__contains=goods)
    lens = len(goods_data)

    # 获取循环获取商品具体信息
    good_info = []
    for i in range(lens):
        goods_info_ = {}
        discount = []

        # 直接在商品表获取商品信息
        goods_info_['goods_id'] = goods_data[i].goods_id
        goods_info_['goods_name'] = goods_data[i].goods_name
        goods_info_['goods_img'] = goods_data[i].goods_img
        goods_info_["goods_introduce"] = goods_data[i].goods_introduce
        goods_info_['goods_price'] = goods_data[i].goods_price
        goods_info_['goods_sales'] = goods_data[i].goods_sales

        # 从多对多数据表种获取商品打折活动信息
        discount_ = goods_data[i].goods.all()
        discount_lens = len(discount_)
        goods_avtivity = []
        for k in range(discount_lens):
            goods_avtivity_ = discount_[k].activity_id.activity_name
            goods_avtivity.append(goods_avtivity_)
        discount.append(goods_avtivity)

        goods_info_['goods_activity'] = discount[0]
        good_info.append(goods_info_)
    # print(good_info)

    if lens:
        data = {
            "status": 200,
            "msg": "查询成功",
            "data": good_info,
        }
    else:
        data = {
            "status": 400,
            "msg": "未匹配到相关数据",
        }

    return JsonResponse(data)
