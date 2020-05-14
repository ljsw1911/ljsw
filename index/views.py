from django.http import JsonResponse

from index.models import Garbage,GarbageType
# Create your views here.


def get_search(request):
    garbage = request.POST.get('garbage')
    # 获取垃圾信息
    garbage_data = Garbage.objects.filter(gar_name__contains=garbage)
    # 获取垃圾类型
    garbage_type = GarbageType.objects.filter(type_id__gar_name__contains=garbage)
    # print(garbage_data)
    # print(garbage_type)
    lens = len(garbage_data)

    result = []
    for i in range(lens):
        garbage = {}

        garbage['gar_id'] = garbage_data[i].gar_id
        garbage['gar_name'] = garbage_data[i].gar_name
        garbage['gar_type_id'] = garbage_data[i].gar_type_id
        garbage['gar_type_name'] = garbage_type[i].gar_type_name
        garbage['gar_introduce'] = garbage_data[i].gar_introduce
        garbage['gar_define'] = garbage_data[i].gar_define
        garbage['gar_guide'] = garbage_data[i].gar_guide

        result.append(garbage)

    if lens:
        data = {
            "status": 200,
            "msg": "查询成功",
            "data":result,
        }
    else:
        data = {
            "status": 400,
            "msg": "未匹配到相关数据",
        }

    return JsonResponse(data = data)