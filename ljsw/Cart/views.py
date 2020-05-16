
from django.http import JsonResponse


# 获取上门回收的信息
from Cart.models import Cart


def cart(request):
    if request.method == 'POST':
        print('***********')
        token = request.GET
        user_id = request.POST.get('user_id')
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


