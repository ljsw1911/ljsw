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
from user.models import User


# Create your views here.
def user_login(request):
    """
    验证验证码登录返回token
    """
    phone = request.POST.get('phone')
    code = request.POST.get('verfy_code')

    key = cache.get('VCODE-{}'.format(phone))
    if key and (key != int(code)):
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
    print(2)
    # user, _ = User.objects.get_or_create(user_phone=phone, defaults={'nikename' == 'u_' + str(phone)})
    print(1)
    get_user = User.objects.get(user_phone=phone)
    token = secrets.token_hex()
    cache.set(get_user.user_id, token, timeout=60 * 60 * 24 * 7)
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
    return None
