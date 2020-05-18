import json

from django.core.cache import cache

from django.http import JsonResponse

from Recycling.models import Recycling


# 获取上门回收的信息
def recycling(request):
    token = request.GET.get('token')
    user_id = cache.get(token)
    if request.method == 'POST':
        recycling_time = request.POST.get('recycling_time')
        print(recycling_time)
        current_time = request.POST.get('current_time')
        print(current_time)
        recycle_msg = request.POST.get('recycle_msg')
        print(recycle_msg)
        recycling_new = Recycling(user_id=user_id, recycling_time=recycling_time, recycle_msg=recycle_msg, current_time=current_time)
        recycling_new.save()
        recycling_dict = {
                          'recycling_id': recycling_new.recycling_id,
                          'recycling_time': recycling_time,
                          'current_time': current_time,
                          'recycle_msg': recycle_msg
                          }
        return JsonResponse(
            {
                'code': 200,
                'msg': '订单添加成功',
                'data': recycling_dict,
            }
        )
    else:
        return JsonResponse(
            {
                'code': 400,
                'msg': '订单添加失败',
            }
        )


