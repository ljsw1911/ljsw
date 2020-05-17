from django.core.cache import cache

from django.http import JsonResponse

from django.utils import timezone

from Order.models import Order

from Order.models import Goods


# 获取订单信息
def order(request):
    token = request.GET.get('token')
    user_id = cache.get(token)
    if request.method == 'POST':
        goods_id = request.POST.get('goods_id')
        or_name = request.POST.get('or_name')
        or_phone = request.POST.get('or_phone')
        or_address = request.POST.get('or_address')
        or_price = request.POST.get('or_price')
        or_freight = request.POST.get('or_freight')
        or_time = timezone.now()
        or_note = request.POST.get('or_note')
        or_num = request.POST.get('or_num')
        order_new = Order(goods_id=goods_id, user_id=user_id, or_name=or_name, or_phone=or_phone, or_address=or_address, or_price=or_price, or_freight=or_freight, or_time=or_time, or_note=or_note, or_num=or_num)
        order_new.save()

        # 修改商品表的库存和已售数量
        goods = Goods.objects.get(goods_id=order_new.goods_id)
        goods.goods_num = int(goods.goods_num) - int(or_num)
        goods.goods_sales = int(goods.goods_sales) + int(or_num)
        goods.save()
        order_dict = {
            'order_id': order_new.order_id,
            'goods_id': goods_id,
            'user_id': user_id,
            'or_name': or_name,
            'or_phone': or_phone,
            'or_num': or_num,
            'or_address': or_address,
            'or_price': or_price,
            'or_freight': or_freight,
            'or_time': or_time,
            'or_status': order_new.or_status,
            'or_note': or_note,
        }
        return JsonResponse(
            {
               'code': 200,
               'msg': '订单添加成功',
               'data': order_dict
            }
        )
    else:
        return JsonResponse(
            {
                'code': 400,
                'msg': '订单添加失败'
            }
        )


