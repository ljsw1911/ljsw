from django.core.cache import cache

from django.http import JsonResponse

from Cart.models import Cart


def cart(request):
    # 加入登录保护，判断用户是否登录
    token = request.GET.get('token')
    try:
        user_id = cache.get(token)
    except Exception as e:
        return JsonResponse({
            'status': 201,
            'msg': 'token失效，请重新登录',
            'data': {}
        })

    # 获取购物车的信息
    if request.method == 'POST':
        goods_id = request.POST.get('goods_id')
        cart_new = Cart(user_id=user_id, goods_id=goods_id)
        cart_new.save()
        cart_id = cart_new.cart_id
        cart_dict = {'cart_id': cart_id, 'user_id': user_id, 'goods_id': goods_id}
        print(cart_dict)
        return JsonResponse(
            {
               'code': 200,
               'msg': '购物车添加成功',
               'data': cart_dict
            }
        )
    else:
        return JsonResponse(
            {
                'code': 400,
                'msg': '购物车添加失败'
            }
        )


