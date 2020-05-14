"""ljsw_obj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from Live import views

urlpatterns = [
    # 生活首页关注页面
    path('index_follow/', views.index_follow, name='index_folow'),
    # 生活首页推荐页面
    path('index_recommend/', views.index_recommend, name='index_recommend'),
    # 生活首页社区页面
    path('index_community/', views.index_community, name='index_community'),
    # 生活首页新闻页面
    path('index_news/', views.index_news, name='index_news'),
    # 生活首页视频页面
    path('index_video/', views.index_video, name='index_video'),
    # 评论信息
    path('comments/', views.coments, name='comments'),
    # 文章发布
    path('article_editor/', views.article_editor, name='article_editor'),

]


