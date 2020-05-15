# 调取cache缓存，查看token中携带的用户id
import secrets

from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.utils import timezone

from django.db.models import Count

import datetime

# 从数据库倒入数据表
from Live.models import ArticlePub, Collection, Praise, Focus, Comments,Goods


# 生活首页关注页面
def index_follow(request):
    return None


# 生活页面-推荐页面
def index_recommend(request):
    # a = request.GET.get('cagetory_id')
    # cageraty = Cageroty.object.filter(pk = int(a))
    data = []
    article_dict = {}
    article = ArticlePub.objects.all()
    # collection = Collection.objects.all()
    # 获取当前用户的id
    # token = request.GET.get('token')
    # read_id = cache.get(token)

    read_id = 1
    for msg in article:
        article_dict['article_title'] = msg.article_title
        article_dict['article_main'] = msg.article_main
        article_dict['article_img"'] = msg.article_img

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

        # 现在要获取该文章收藏的次数
        collection_dict = Collection.objects.filter(article_id=msg.artilce_id).aggregate(
            num=Count('user_id'))
        article_dict['collection_num'] = collection_dict['num']

        # 当前用户是否收藏了该文章
        collection_user_id = Collection.objects.filter(article_id=msg.artilce_id)
        # print(collection_user_id) 这是一个object类型就可以直接调用表的数据
        for i in collection_user_id:
            if i.user_id == read_id:
                article_dict['collection_info'] = 1
                break
        else:
            article_dict['collection_info'] = 0

        # 查询点赞人数，并且查看当前用户是否点赞了该文章
        praise_dict = Praise.objects.filter(article_id=msg.artilce_id).aggregate(num=Count('user_id'))
        article_dict['praise_num'] = praise_dict['num']
        praise_user_id = Praise.objects.filter(article_id=msg.artilce_id)
        for i in praise_user_id:
            if i.user_id == read_id:
                article_dict['praise_info'] = 1
                break
        else:
            article_dict['praise_info'] = 0

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
        'msg': '数据传输成功',
        'data': data,
    })


# 生活首页社区页面
def index_community(request):
    pass


# 生活首页新闻页面
def index_news(request):
    pass


# 生活首页视频页面
def index_video(request):
    pass


def coments(request):
    data = []
    comments_dict = {}
    article = ArticlePub.objects.all()
    for msg in article:
        comment_user_id = Comments.objects.filter(article_id=msg.artilce_id)
        comments_dict[msg.artilce_id] = msg.artilce_id
        for i in comment_user_id:
            comments_dict[i.user_id] = i.comment
        data.append(comments_dict)
        comments_dict = {}
    return JsonResponse({
        'code': 200,
        'msg': '评论信息',
        'comments': data,
    })


def article_editor(request):
    if request.method == 'POST':

        article = ArticlePub()
        article_title = request.POST.get('article_title')
        article_main = request.POST.get('article_main')
        # author_id = cache.get('token')
        author_id = 4

        article.article_title = article_title
        article.article_main = article_main
        article.article_datatime = datetime.datetime.now()
        article.article_video = 0
        article.author_id = author_id
        article.save()

        data = {
            'article_title': article_title,
            'article_main': article_main,
            'article_datatime': datetime.datetime.now(),
            'rticle_video': 0,
            'author_id ': author_id,
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

'''

根据前端的token值获取当前用户的id

def get_user_id(request):
    token = request.GET.get('token')
    uid = cache.get(token)
    return JsonResponse({
        'uid':int(uid)
    })


def login(request):
    if request.method == 'POST':
        uid = request.POST.get('uid')
        token = secrets.token_hex()
        cache.set(token, uid, timeout=60 * 60)
        return JsonResponse({
            'code': 200,
            'msg': '登陆成功',
            'token': token,
        })

'''

# 商品的
def market_index(request):
    goods_list = []
    goods_dict = {}
    goods = Goods.objects.all()
    for msg in goods:
        goods_dict['goods_id'] = msg.goods_id
        goods_dict['goods_name'] = msg.goods_name
        goods_dict['goods_img'] = msg.goods_img
        goods_dict['goods_introduce'] = msg.goods_introduce
        goods_dict['goods_price'] = msg.goods_price
        goods_dict['goods_sales'] = msg.goods_sales

        goods_list.append(goods_dict)
        goods_dict = {}

    return JsonResponse({
        'code':200,
        'msg':'商品信息展示',
        'goods_list':goods_list
    })