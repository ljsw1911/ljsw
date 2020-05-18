from django.core.cache import cache

from django.http import JsonResponse

from Cart.models import Cart


# 获取购物车的信息
def cart(request):
    token = request.GET.get('token')
    user_id = cache.get(token)
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


