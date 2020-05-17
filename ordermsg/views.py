from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse

# Create your views here.
from common import errors
from ordermsg.models import User, Order, Goods


def ordermsg(request):
    """
    点击分别展示 代付款 配送中  完成页面 默认全部
    :param request:
    :return:
    """
    token = request.GET.get('token')
    uid = cache.get(token)
    state = request.GET.get('orders_status')

    if int(state) == 3:
        orders = Order.objects.filter(user_id=uid).all()
    else:
        orders = Order.objects.filter(user_id=uid).filter(or_status=state).all()
    if orders:
        data = []
        for order in orders:
            good_id = order.goods_id
            goods = Goods.objects.filter(pk=good_id).first()
            goods_img = goods.goods_img.split(',')[0]
            data.append({
                'order_id': '8801-7780-' + str(order.order_id),
                'or_price': order.or_price,
                'goods_name': goods.goods_name,
                'gooed_img': goods_img,
                'goods_introduce': goods.goods_introduce,
                'or_num': order.or_num,
                'or_status': order.or_status,
            })
        return JsonResponse({
            "status": 200,
            "msg": "ok",
            "data": data
        })

    return JsonResponse({
        "status": 201,
        "msg": "查询无",
        "data": ""
    })




def orderinfo(request):
    """
    通过获取所在页面的订单号 给订单页面详情
    :param request:
    :return:
    """
    token = request.GET.get('token')
    uid = cache.get(token)
    order_id = request.GET.get('order_id')
    rec_id = str(order_id).split('8801-7780-')[1]

    order = Order.objects.filter(user_id=uid).filter(pk=rec_id).first()
    if order:
        good_id = order.goods_id
        goods = Goods.objects.filter(pk=good_id).first()
        goods_img = goods.goods_img.split(',')[0]
        point = order.or_price % 100
        data = {
            'order_id': '8801-7780-' + str(order.order_id),
            'or_price': order.or_price,
            'goods_name': goods.goods_name,
            'gooed_img': goods_img,
            'goods_introduce': goods.goods_introduce,
            'or_num': order.or_num,
            'points': point,
            'freight': goods.goods_freight,
            'name': order.or_name,
            'phone': order.or_phone,
            'addres': order.or_address,
        }
        return JsonResponse({
            "status": 200,
            "msg": "ok",
            "data": data
        })

    return JsonResponse(errors.error400)


def complete(request):
    """
    订单收货确认
    :param request:
    :return:
    """
    token = request.GET.get('token')
    uid = cache.get(token)
    state = request.GET.get('orders_status')
    order_id = request.GET.get('order_id')

    rec_id = str(order_id).split('8801-7780-')[1]
    order = Order.objects.filter(user_id=uid).filter(pk=rec_id).first()
    if order:
        if int(state) == 1:
            order.recycle_state = 2
            point = order.or_price % 100
            user = User.objects.get(pk=uid)
            user.now_integral += point
            user.add_integral += point
            user.save()
            order.save()
            return JsonResponse({
                "status": 200,
                "msg": "完成订单",
                'rec_state': 2
            })
        else:
            order.recycle_state = 2
            order.save()
            return JsonResponse({
                "status": 201,
                "msg": "取消成功",
                'or_status': 2
            })

    return JsonResponse(errors.error400)


def pay(request):
    return None


def delete(request):
    """
    删除订单
    :param request:
    :return:
    """
    token = request.GET.get('token')
    uid = cache.get(token)
    order_id = request.GET.get('order_id')

    rec_id = str(order_id).split('8801-7780-')[1]
    order = Order.objects.filter(user_id=uid).filter(pk=rec_id).first()
    if order:
        order.delete()
        return JsonResponse({
            {
                "status": 200,
                "msg": "删除成功",
            }
        })
    return JsonResponse(errors.error400)
