import json

from django.http import HttpResponse

from Recycling.models import Recycling


# 获取上门回收的信息
def recycling(request):
    if request.method == 'POST':
        # user_id = request.POST.get('user_id')
        recycling_time = request.POST.get('recycling_time')
        print(recycling_time)
        current_time = request.POST.get('current_time')
        print(current_time)
        recycle_msg = request.POST.get('recycle_msg')
        print(recycle_msg)
        recycling_new = Recycling(recycling_time=recycling_time, recycle_msg=recycle_msg, current_time=current_time)
        recycling_new.save()
        recycling_dict = {'recycling_id': recycling_new.recycling_id, 'recycling_time': recycling_time, 'current_time': current_time, 'recycle_msg': recycle_msg}
        return HttpResponse(json.dumps(recycling_dict, ensure_ascii=False), content_type="application/json,charset=utf-8")
    return HttpResponse('这个暂时没用')

