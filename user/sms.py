#!/usr/bin/env python
# coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

ACCESS_KEY_ID = ""  # 用户AccessKey  需要根据自己的账户修改
ACCESS_KEY_SECRET = ""  # Access Key Secret  需要根据自己的账户修改


class SMS:

    def __init__(self):
        self.signName = "红茶不加冰"  # 签名
        self.templateCode = "SMS_185840990"  # 模板code
        self.client = client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, 'cn-hangzhou')

    def send(self, phone_num, Param):
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('dysmsapi.aliyuncs.com')
        request.set_method('POST')
        request.set_protocol_type('https')  # https | http
        request.set_version('2017-05-25')
        request.set_action_name('SendSms')

        request.add_query_param('RegionId', "cn-hangzhou")
        request.add_query_param('PhoneNumbers', phone_num)
        request.add_query_param('SignName', self.signName)
        request.add_query_param('TemplateCode', self.templateCode)
        request.add_query_param('TemplateParam',  Param)  # "{\"code\":\"2222\"}"

        response = self.client.do_action(request)
        # python2:  print(response)
        # print(str(response, encoding='utf-8'))
        return response

