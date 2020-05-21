import secrets

from django.core.cache import cache
from django.db.models import Count
from django.http import JsonResponse

from django.core.files.uploadedfile import InMemoryUploadedFile

import datetime

from django.utils import timezone

from live_live.upload_qiniuyun import storage_img
# 从数据库倒入数据表
from live_live.models import ArticlePub, Collection, Praise, Focus


# 生活-生活首页
def index(request):
    # token = request.GET.get('token')
    # read_id = cache.get(token)
    read_id = 4
    data = []
    article_dict = {}


    category_id = request.GET.get('category_id')
    # category_id = 2
    articles = ArticlePub.objects.filter(category_id=category_id)

    for msg in articles:
        img = {}
        article_dict['article_title'] = msg.article_title
        article_dict['article_main'] = msg.article_main
        img['type'] = msg.type
        img['img_url'] = msg.article_pic.split(',')
        article_dict['img'] = img
        before = timezone.now() - msg.article_datatime
        if before.days == 0:
            before_list = str(before).split(':')
            if int(before_list[0]) > 0:
                before = before_list[0] + '小时前'
            else:
                before = before_list[1] + '分钟前'
        else:
            # 如果大于一天则显示文章发布的时间
            before = msg.article_datatime.strftime('%Y年%m月%d日')
        article_dict['data'] = before

        # 查询点赞人数，并且查看当前用户是否点赞了该文章
        praise_dict = Praise.objects.filter(article_id=msg.article_id).aggregate(num=Count('user_id'))
        article_dict['praise_num'] = praise_dict['num']
        praise_user_id = Praise.objects.filter(article_id=msg.article_id)
        for i in praise_user_id:
            if i.user_id == read_id:
                article_dict['praise_info'] = 1
                break
        else:
            article_dict['praise_info'] = 0

        # 现在要获取该文章收藏的次数
        collection_dict = Collection.objects.filter(article_id=msg.article_id).aggregate(
            num=Count('user_id'))
        article_dict['collection_num'] = collection_dict['num']

        # 当前用户是否收藏了该文章
        collection_user_id = Collection.objects.filter(article_id=msg.article_id)
        # print(collection_user_id) 这是一个object类型就可以直接调用表的数据
        for i in collection_user_id:
            if i.user_id == read_id:
                article_dict['collection_info'] = 1
                break
        else:
            article_dict['collection_info'] = 0

        # 当前用户是否关注了某个文章的作者
        focus_user_id = Focus.objects.filter(author_id=msg.author_id)
        for i in focus_user_id:
            print(i.user_id)
            if i.user_id == read_id:
                article_dict['focus_info'] = 1
                break
        else:
            article_dict['focus_info'] = 0

        data.append(article_dict)
        article_dict = {}

    return JsonResponse({
        'code': 200,
        'msg': '文章数据',
        'data': data,
    })


# 生活-文章编辑
def article_editor(request):
    if request.method == 'POST':
        video = {'avi', 'wmv', 'mpg', 'mov', 'rm', 'swf', 'mp4'}
        article = ArticlePub()
        article_title = request.POST.get('article_title')
        article_main = request.POST.get('article_main')
        # 获取照片的地址
        picture_url_list = []
        img = request.FILES.getlist('article_pic')
        for msg in img:
            img_suffix = str(msg).split('.')[-1]
            result = storage_img(msg.read(),img_suffix)
            picture_url_list.append(result)
        picture_url = ','.join(picture_url_list)
        article.article_pic = picture_url
        # print(len(picture_url_list))
        if len(picture_url_list) == 1:
            img_suffix = picture_url_list[0].split('/')[-1]
            # print(img_suffix)
            if img_suffix in video:
                type = 'video'
            else:
                type = 'img'
        else:
            type = 'img'

        category_id = 3
        # request.GET.get('token')
        # author_id = cache.get('token')
        author_id = 8

        article.article_title = article_title
        article.article_main = article_main
        article.article_datatime = datetime.datetime.now()
        article.category_id = category_id
        article.author_id = author_id
        article.type = type
        article.save()

        data = {
            'article_title': article_title,
            'article_main': article_main,
            'article_datatime': datetime.datetime.now(),
            'category_id': category_id,
            'author_id ': author_id,
            'article_pic': picture_url,
            'type': type
        }
        return JsonResponse({
            'code': 200,
            'msg': '文章发布成功',
            'data': data
        })
    else:
        return JsonResponse({
            'code': 400,
            'msg': '文章添加失败'
        })
