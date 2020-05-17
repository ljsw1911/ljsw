'''
author = 李雄涛
data = 2020/5/16
当前py文件的作用：将本地照片和视频上传七牛云
'''

from qiniu import Auth, put_file, etag, put_data
import qiniu.config


def upload(avatar,name):
    # 需要填写你的 Access Key 和 Secret Key
    access_key = 'tYEJjcDsjTDnrhcAsFDK68Fxg8Tho10lo8gy-G3s'
    secret_key = 'I3d1WffCP6cIAuHoiObjUkce18d1Pwo3FBwnYrbS'
    # 构建鉴权对象
    q = Auth(access_key, secret_key)
    # 要上传的空间

    bucket_name = 'ljsw-avatars'
    # 要上传文件的本地路径
    # url = 'http://qafhdvs6m.bkt.clouddn.com/'
    # for msg in photo:
    # 上传后保存的文件名
    key =  name
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    localfile = 'static/upload/avatars/' + name
    ret, info = put_file(token, key, localfile)

    # assert ret['key'] == key
    # assert ret['hash'] == etag(localfile)
    if info.status_code == 200:
        return ret.get('key')
    else:
        raise Exception('上传失败')
