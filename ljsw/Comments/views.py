
from django.http import JsonResponse

from Comments.models import ArticlePub

from Comments.models import Comments

from Comments.models import User


# 展示消息界面的信息
def comment(request):
    if request.method == 'POST':
        comments = Comments.objects.all()
        for comm in comments:
            comment_names = User.objects.filter(user_id=comm.comment_user_id)
            for comment_name in comment_names:
                comment_title = comm.comment
                print(comment_title)
                print(comm.article_id)
                articles = ArticlePub.objects.filter(article_id=comm.article_id)
                for article in articles:
                    article_names = User.objects.filter(user_id=article.author_id)
                    for article_name in article_names:
                        article_titles = ArticlePub.objects.filter(article_id=comm.article_id)
                        for article_title in article_titles:
                            data = {
                                'comment_name': comment_name.nickname,
                                'comment_title': comment_title,
                                'article_name': article_name.nickname,
                                'article_title': article_title.article_title,
                            }
                            print(data)
                            return JsonResponse(
                                {
                                    'code': 200,
                                    'msg': '评论数据发送成功',
                                    'data': data,
                                }
                            )

    else:
        return JsonResponse(
            {
                'code': 400,
                'msg': '评论数据发送失败',
            }
        )


