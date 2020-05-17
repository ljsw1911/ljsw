import random
import re
import json
import secrets

from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render
import requests

from ljsw import settings
from user.sms import SMS
from user.models import User, Addres, DetailedPoints, Recycling
from common import errors


# Create your views here.
def user_login(request):
    """
    验证验证码登录返回token
    """
    phone = request.POST.get('phone')
    code = request.POST.get('verfy_code')

    key = cache.get('VCODE-{}'.format(phone))
    if key != int(code):
        data = {
            "status": 400,
            "msg": "验证码错误"
        }
        return JsonResponse(data=data)

    try:  # 是否注册过
        User.objects.get(user_phone=phone)
    except User.DoesNotExist:
        user = User()
        user.user_phone = phone
        user.nickname = 'u_' + str(phone)
        try:
            user.save()

        except Exception as e:
            data = {
                "status": 400,
                "msg": "错误:" + str(e)
            }
            return JsonResponse(data=data)
    get_user = User.objects.get(user_phone=phone)
    token = secrets.token_hex()
    cache.set(token, get_user.user_id, timeout=60 * 60 * 24 * 7)
    print(token)
    data = {
        "status": 200,
        "msg": "登录成功",
        "data": {
            "token": token
        }
    }
    return JsonResponse(data=data)


def user_inspect(request):
    """
    判断手机号
    :param request:phone
    :return: 是否符合手机类型
    """
    res_phone = request.POST.get('phone')
    inspect = re.match(r"^1[35678]\d{9}$", res_phone)
    if inspect:
        data = {'status': 200,
                'msg': '手机号可用'
                }
    else:
        data = {'status': 400,
                'msg': '手机格式错误'
                }
    return JsonResponse(data=data)


def get_code(request):
    """
    发送验证码
    :param request:
    :return: 验证码发送成功
    """
    rs_get_phone = request.POST.get('phone')
    sms = SMS()

    def gen_vcode(size=6):
        start = 10 ** (size - 1)
        end = 10 ** size - 1
        return random.randint(start, end)

    vcode = gen_vcode()
    key = 'VCODE-{}'.format(rs_get_phone)

    sms_code = "{'code':'%d'}" % vcode
    res = sms.send(rs_get_phone, sms_code)
    js = json.loads(res)
    cn = js['Message']
    timeout = 60 * 60 * 24 if settings.DEBUG else 180
    cache.set(key, vcode, timeout=timeout)  # 存入缓存
    if cn == "OK":
        data = {
            "status": 200,
            "msg": "验证码发送成功"
        }
    else:
        data = {
            "status": 400,
            "msg": "验证码发送失败"
        }
    return JsonResponse(data=data)


def userinfo(request):
    """
    获取token值来得到用户id
    :param request:
    :return:
    """
    token = request.GET.get('token')

    try:
        uid = cache.get(token)
    except Exception as e:
        return JsonResponse({
            'status': 201,
            'msg': 'token失效，请重新登录',
            'data': {}
        })
    try:
        user = User.objects.get(pk=uid)
    except Exception as e:
        return JsonResponse({
            'code': 400,
            'msg': '该用户不存在',
            'data': {}
        })
    obj = str(user.avatar)
    if obj:
        obj = 'http://www.yichr.cn/static/upload/' + obj

    return JsonResponse({
        'status': 200,
        'msg': '信息获取成功',
        'data': {
            'uid': uid,
            'nikename': user.nickname,
            "phone": user.user_phone,
            "avatar": obj,
            "recycle": user.recycle_num,
            "now_integral": user.now_integral,
            "add_integral": user.add_integral,
            "signature": user.signature
        }
    })


def modify(request):
    token = request.GET.get('token')
    uid = cache.get(token)
    """
    通过 获取 token 得到 userid 匹配id修改信息 
    """
    nickname = request.POST.get('nickname')
    avatar = request.FILES.get('avatar')
    gender = request.POST.get('gender')
    birthday = request.POST.get('birthday')
    signature = request.POST.get('signature')
    try:
        user = User.objects.get(user_id=uid)
    except:
        return JsonResponse({
            'status': 400,
            'msg': 'tokens失效',
            'data': {}
        })
    if gender == '男':
        gender = 0
    elif gender == '女':
        gender = 1
    else:
        gender = 0
    if birthday:
        user.birthday = birthday
    user.nickname = nickname
    user.avatar = avatar
    user.gender = gender
    user.signature = signature
    user.save()
    return JsonResponse({
        'status': 200,
        'msg': '修改成功',
    })


def get_msg(request):
    """
    获取用户修改界面信息
    :param request:
    :return:
    """
    token = request.GET.get('token')
    uid = cache.get(token)

    try:
        user = User.objects.get(user_id=uid)
    except:
        return JsonResponse({
            'status': 400,
            'msg': 'tokens失效',
            'data': {}
        })

    avatar = user.avatar
    img = str(avatar)
    if avatar:
        img = 'http://www.yichr.cn/static/upload/' + img

    return JsonResponse({
        'status': 200,
        'msg': '获取成功',
        'data': {
            'nikename': user.nickname,
            "avatar": img,
            "gender": user.gender,
            "birthday": user.birthday,
            "signature": user.signature
        }
    })


def addres(request):
    """
    获取地址
    :param request:
    :return:
    """
    token = request.GET.get('token')
    uid = cache.get(token)

    u_addres = Addres.objects.filter(user_id=uid).all()
    if u_addres:
        data = []
        for add in u_addres:
            data.append({
                'addres_id': add.address_id,
                'addres': add.estate + add.building + add.room,
                'identity': add.identity
            })
        return JsonResponse({
            'status': 200,
            'msg': '获取成功',
            'data': data
        })
    else:
        return JsonResponse({
            'status': 500,
            'msg': '获取成功',
            'data': ""
        })


def mod_addres(request):
    """
    修改地址
    :param request:
    :return:
    """
    token = request.GET.get('token')
    add_id = request.GET.get('addres_id')
    uid = cache.get(token)

    estate = request.POST.get('estate')
    building = request.POST.get('building')
    room = request.POST.get('room')
    identity = request.POST.get('identity')
    if add_id:
        try:
            u_addres = Addres.objects.filter(user_id=uid).get(pk=add_id)
            u_addres.estate = estate
            u_addres.building = building
            u_addres.room = room
            u_addres.identity = identity
            try:
                u_addres.save()
                return JsonResponse({
                    'status': 200,
                    'msg': '修改成功',
                    'data': ""
                })
            except Exception as e:
                print(e)
        except Exception as e:
            return JsonResponse({
                'status': 400,
                'msg': '无效地址',
                'data': ""
            })
    if estate or building or room:
        u_addres = Addres()
        u_addres.user_id = uid
        u_addres.estate = estate if estate else ' '
        u_addres.building = building if building else ' '
        u_addres.room = room if room else ' '
        u_addres.identity = identity
        try:
            u_addres.save()
            return JsonResponse({
                'status': 201,
                'msg': '创建成功',
                'data': ""
            })
        except Exception as e:
            print(e)
    return JsonResponse({
        'status': 400,
        'msg': '无效地址',
        'data': ""
    })


def del_addres(request):
    """
    删除地址
    :param request:
    :return:
    """
    token = request.GET.get('token')
    add_id = request.GET.get('addres_id')
    uid = cache.get(token)

    u_addres = Addres.objects.filter(user_id=uid).filter(pk=add_id).first()
    if u_addres:
        u_addres.delete()
        data = {
            "status": 200,
            "msg": "删除成功"
        }
        return JsonResponse(data=data)

    data = {
        "status": 400,
        "msg": "失败"
    }
    return JsonResponse(data=data)


def mod_addres_single(request):
    """
    修改地址信息显示
    :param request:
    :return:
    """
    token = request.GET.get('token')
    add_id = request.GET.get('addres_id')
    uid = cache.get(token)
    try:
        u_addres = Addres.objects.filter(user_id=uid).get(pk=add_id)
        data = {
            'estate': u_addres.estate,
            'roommsg': u_addres.building + u_addres.room,
            'identity': u_addres.identity
        }
        return JsonResponse({
            'status': 200,
            'msg': 'ok',
            'data': data
        })
    except:
        pass
    return JsonResponse({
        'status': 400,
        'msg': '获取信息失败',
        'data': ""
    })


def points(request):
    """
    获取积分明细
    :param request:
    :return:
    """
    token = request.GET.get('token')
    points = request.GET.get('points')
    point_msg = request.GET.get('pointmsg')
    uid = cache.get(token)

    if uid:
        user = User.objects.filter(pk=uid).first()
        if user:
            user.now_integral += int(points)
            user.add_integral += int(points)
            point_create = DetailedPoints()
            point_create.user_id = uid
            point_create.points_num = points
            point_create.point_type = point_msg
            point_create.save()
            user.save()
            return JsonResponse({
                'status': 200,
                'msg': '存储成功',
            })
    return JsonResponse(errors.error400)


def points_form(request):
    """
    返回积分明细
    :param request:
    :return:
    """
    token = request.GET.get('token')
    uid = cache.get(token)
    point_msg = DetailedPoints.objects.filter(user_id=uid).all()
    if point_msg:
        data = []
        for msg in point_msg:
            msg_time = msg.points_time
            msg_time = str(msg_time).split('T')[0]
            data.append({
                'points_msg': msg.point_type,
                'points': msg.points_num,
                'point_time': msg_time
            })
        return JsonResponse({
            'status': 200,
            'msg': 'ok',
            'data': data
        })

    return JsonResponse(errors.error400)


def exchange(request):
    """
    兑换积分
    :param request:
    :return:
    """
    token = request.GET.get('token')
    uid = cache.get(token)
    points = request.GET.get('exchange')
    print(points)
    print(type(points))
    if points and int(points) != 0:
        user = User.objects.filter(pk=uid).first()
        if user:
            point = user.now_integral if int(points) > user.now_integral else int(points)
            user.now_integral -= point
            user.save()
            point_create = DetailedPoints()
            point_create.user_id = uid
            point_create.points_num = point
            point_create.point_type = '兑换{}积分'.format(point)
            user.save()
            point_create.save()

            return JsonResponse({
                'status': 200,
                'msg': '兑换成功',
            })

    return JsonResponse(errors.error400)


def recycle_order(request):
    """
    获取上门订单信息
    :param request:
    :return:
    """
    token = request.GET.get('token')
    uid = cache.get(token)

    recycles = Recycling.objects.filter(user_id=uid).all()
    user = User.objects.filter(user_id=uid).first()

    if recycles and user:
        data = []
        for recycle in recycles:
            addres = Addres.objects.get(address_id=recycle.addres_id)
            recycling_time = str(recycle.recycling_time).split('T')[0]
            current_time = str(recycle.current_time).split('T')[0]
            data.append({
                'recyling_id': '8801-9587-' + str(recycle.recycling_id),
                'recycling_time': recycling_time,
                'current_time': current_time,
                'addres': addres.estate + addres.building + addres.room,
                'recycle_state': recycle.recycle_state,
                'phone': user.user_phone

            })
        return JsonResponse({
            "status": 200,
            "msg": "ok",
            "data": data
        })
    return JsonResponse(errors.error400)


def recycle_order_choice(request):
    """
    点击分别展示 预约中 已预约 完成页面
    :param request:
    :return:
    """
    token = request.GET.get('token')
    uid = cache.get(token)
    state = request.GET.get('recycle_state')

    recycles = Recycling.objects.filter(user_id=uid).filter(recycle_state=state).all()
    user = User.objects.filter(user_id=uid).first()

    if recycles and user:
        data = []
        for recycle in recycles:
            addres = Addres.objects.get(address_id=recycle.addres_id)
            recycling_time = str(recycle.recycling_time).split('T')[0]
            current_time = str(recycle.current_time).split('T')[0]
            data.append({
                'recyling_id': '8801-9587-' + str(recycle.recycling_id),
                'recycling_time': recycling_time,
                'current_time': current_time,
                'addres': addres.estate + addres.building + addres.room,
                'recycle_state': recycle.recycle_state,
                'phone': user.user_phone
            })
        return JsonResponse({
            "status": 200,
            "msg": "ok",
            "data": data
        })
    return JsonResponse(errors.error400)


def rec_com_cle(request):
    """
    通过获取所在页面的订单号 给定不同完成字段
    :param request:
    :return:
    """
    token = request.GET.get('token')
    uid = cache.get(token)
    state = request.GET.get('rec_state')
    recyling_id = request.GET.get('recyling_id')
    rec_id = recyling_id.split('8801-9587-')[1]

    recycle = Recycling.objects.filter(user_id=uid).filter(pk=rec_id).first()
    if recycle:
        if int(state) == 1:
            recycle.recycle_state = 2
            recycle.save()
            return JsonResponse({
                "status": 200,
                "msg": "完成服务",
                'rec_state':state
            })
        else:
            recycle.recycle_state = 2
            recycle.save()
            return JsonResponse({
                "status": 201,
                "msg": "取消成功",
                'rec_state': state
            })
    return JsonResponse(errors.error400)
