'''
author = 李雄涛
data = 2020/5/16
当前py文件的作用：将本地照片和视频上传七牛云
'''

from qiniu import Auth, put_data
import qiniu.config
'''
#需要填写你的 Access Key 和 Secret Key
access_key = 'tYEJjcDsjTDnrhcAsFDK68Fxg8Tho10lo8gy-G3s'
secret_key = 'I3d1WffCP6cIAuHoiObjUkce18d1Pwo3FBwnYrbS'
#构建鉴权对象
q = Auth(access_key, secret_key)
#要上传的空间
bucket_name = 'ljsw-article'
#要上传文件的本地路径
photo = ['3.jpg','7.jpg','8.jpg','10.jpg','14.jpg','18.jpg']
url = 'http://qaewhn5po.bkt.clouddn.com/'
for msg in photo:
    # 上传后保存的文件名
    key = 'my-python-'+msg
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    localfile = 'static/'+msg
    ret, info = put_file(token, key, localfile)
    # 这要添加进数据库
    url = url + key
    print(url)
    url = 'http://qaewhn5po.bkt.clouddn.com/'
    print(ret)
    assert ret['key'] == key
    assert ret['hash'] == etag(localfile)

'''


def storage_img(file_data,img_suffix):
    url = 'http://qaewhn5po.bkt.clouddn.com/'
    access_key = 'tYEJjcDsjTDnrhcAsFDK68Fxg8Tho10lo8gy-G3s'
    secret_key = 'I3d1WffCP6cIAuHoiObjUkce18d1Pwo3FBwnYrbS'
    q = Auth(access_key, secret_key)
    #要上传的空间
    bucket_name = 'ljsw-article'
    token = q.upload_token(bucket_name, None, 3600)
    ret, info = put_data(token, None, file_data)
    url = url + str(ret.get('key')) + '/' + img_suffix
    if info.status_code == 200:
        return url
    else:
        raise Exception('上传失败')